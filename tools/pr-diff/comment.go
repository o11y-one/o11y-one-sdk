package main

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"strings"
)

// CommentPoster is the network boundary. render.go's Render is a pure
// function; everything that talks to GitHub lives behind this interface so
// the render core — and the upsert-vs-create decision — can be unit tested
// with fakeCommentPoster in comment_test.go without a socket.
type CommentPoster interface {
	// ListComments returns the existing issue/PR comment bodies, in the API's
	// paging order, id first.
	ListComments(ctx context.Context, owner, repo string, prNumber int) ([]postedComment, error)
	// CreateComment posts a brand-new comment.
	CreateComment(ctx context.Context, owner, repo string, prNumber int, body string) error
	// UpdateComment replaces the body of an existing comment by id.
	UpdateComment(ctx context.Context, owner, repo string, commentID int64, body string) error
}

type postedComment struct {
	ID   int64
	Body string
}

// Upsert finds the first comment containing marker and replaces its body;
// otherwise it creates a new one. This is the idempotent-update behavior the
// task calls for: a re-run on the same PR edits its own prior comment instead
// of stacking a new one on top of it. It is a free function over the
// CommentPoster interface (not a method), so it is exercised in
// comment_test.go against a fake with no network involved.
func Upsert(ctx context.Context, cp CommentPoster, owner, repo string, prNumber int, marker, body string) error {
	existing, err := cp.ListComments(ctx, owner, repo, prNumber)
	if err != nil {
		return fmt.Errorf("listing existing comments: %w", err)
	}
	for _, c := range existing {
		if strings.Contains(c.Body, marker) {
			if err := cp.UpdateComment(ctx, owner, repo, c.ID, body); err != nil {
				return fmt.Errorf("updating comment %d: %w", c.ID, err)
			}
			return nil
		}
	}
	if err := cp.CreateComment(ctx, owner, repo, prNumber, body); err != nil {
		return fmt.Errorf("creating comment: %w", err)
	}
	return nil
}

// githubComments is the real CommentPoster, talking to the GitHub REST API
// (issues/comments — PRs are issues for commenting purposes). Deliberately
// thin: pagination, auth, and JSON (de)serialization only. No rendering
// decisions live here.
type githubComments struct {
	httpClient *http.Client
	baseURL    string // e.g. "https://api.github.com"; overridable for GHES
	token      string
}

// NewGitHubComments builds the real, network-talking CommentPoster. token is
// the GITHUB_TOKEN (or a PAT) with pull-requests: write / issues: write.
func NewGitHubComments(httpClient *http.Client, baseURL, token string) CommentPoster {
	if httpClient == nil {
		httpClient = http.DefaultClient
	}
	if baseURL == "" {
		baseURL = "https://api.github.com"
	}
	return &githubComments{httpClient: httpClient, baseURL: strings.TrimRight(baseURL, "/"), token: token}
}

type ghComment struct {
	ID   int64  `json:"id"`
	Body string `json:"body"`
}

func (g *githubComments) do(ctx context.Context, method, path string, payload any, out any) error {
	var reqBody io.Reader
	if payload != nil {
		buf, err := json.Marshal(payload)
		if err != nil {
			return err
		}
		reqBody = bytes.NewReader(buf)
	}
	req, err := http.NewRequestWithContext(ctx, method, g.baseURL+path, reqBody)
	if err != nil {
		return err
	}
	req.Header.Set("Accept", "application/vnd.github+json")
	req.Header.Set("X-GitHub-Api-Version", "2022-11-28")
	if g.token != "" {
		req.Header.Set("Authorization", "Bearer "+g.token)
	}
	if payload != nil {
		req.Header.Set("Content-Type", "application/json")
	}
	resp, err := g.httpClient.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return err
	}
	if resp.StatusCode >= 300 {
		return fmt.Errorf("github %s %s: status %d: %s", method, path, resp.StatusCode, string(body))
	}
	if out != nil {
		if err := json.Unmarshal(body, out); err != nil {
			return fmt.Errorf("decoding github response from %s %s: %w", method, path, err)
		}
	}
	return nil
}

func (g *githubComments) ListComments(ctx context.Context, owner, repo string, prNumber int) ([]postedComment, error) {
	var page []ghComment
	path := fmt.Sprintf("/repos/%s/%s/issues/%d/comments?per_page=100", owner, repo, prNumber)
	if err := g.do(ctx, http.MethodGet, path, nil, &page); err != nil {
		return nil, err
	}
	out := make([]postedComment, 0, len(page))
	for _, c := range page {
		out = append(out, postedComment{ID: c.ID, Body: c.Body})
	}
	return out, nil
}

func (g *githubComments) CreateComment(ctx context.Context, owner, repo string, prNumber int, body string) error {
	path := fmt.Sprintf("/repos/%s/%s/issues/%d/comments", owner, repo, prNumber)
	return g.do(ctx, http.MethodPost, path, map[string]string{"body": body}, nil)
}

func (g *githubComments) UpdateComment(ctx context.Context, owner, repo string, commentID int64, body string) error {
	path := fmt.Sprintf("/repos/%s/%s/issues/comments/%d", owner, repo, commentID)
	return g.do(ctx, http.MethodPatch, path, map[string]string{"body": body}, nil)
}
