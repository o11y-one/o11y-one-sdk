package main

import (
	"context"
	"testing"
)

// fakeCommentPoster is an in-memory CommentPoster used to test Upsert's
// find-or-create logic without a network call, per the task's "no network in
// tests" gate.
type fakeCommentPoster struct {
	nextID   int64
	comments []postedComment

	listCalls   int
	createCalls int
	updateCalls int
}

func (f *fakeCommentPoster) ListComments(_ context.Context, _, _ string, _ int) ([]postedComment, error) {
	f.listCalls++
	out := make([]postedComment, len(f.comments))
	copy(out, f.comments)
	return out, nil
}

func (f *fakeCommentPoster) CreateComment(_ context.Context, _, _ string, _ int, body string) error {
	f.createCalls++
	f.nextID++
	f.comments = append(f.comments, postedComment{ID: f.nextID, Body: body})
	return nil
}

func (f *fakeCommentPoster) UpdateComment(_ context.Context, _, _ string, commentID int64, body string) error {
	f.updateCalls++
	for i, c := range f.comments {
		if c.ID == commentID {
			f.comments[i].Body = body
			return nil
		}
	}
	return errCommentNotFound(commentID)
}

type errCommentNotFound int64

func (e errCommentNotFound) Error() string { return "comment not found" }

func TestUpsertCreatesOnFirstRun(t *testing.T) {
	fp := &fakeCommentPoster{}
	if err := Upsert(context.Background(), fp, "o11y-one", "sdk", 42, commentMarker, "first render"); err != nil {
		t.Fatalf("Upsert: %v", err)
	}
	if fp.createCalls != 1 || fp.updateCalls != 0 {
		t.Fatalf("first run: got create=%d update=%d, want create=1 update=0", fp.createCalls, fp.updateCalls)
	}
	if len(fp.comments) != 1 || fp.comments[0].Body != "first render" {
		t.Fatalf("unexpected comment state: %+v", fp.comments)
	}
}

// TestUpsertUpdatesOnRerunInsteadOfStacking is the load-bearing test for the
// "idempotent update" requirement: a second render for the same PR must edit
// the existing marked comment, not add a second one.
func TestUpsertUpdatesOnRerunInsteadOfStacking(t *testing.T) {
	fp := &fakeCommentPoster{}
	ctx := context.Background()

	if err := Upsert(ctx, fp, "o11y-one", "sdk", 42, commentMarker, commentMarker+"\nfirst render"); err != nil {
		t.Fatalf("first Upsert: %v", err)
	}
	if err := Upsert(ctx, fp, "o11y-one", "sdk", 42, commentMarker, commentMarker+"\nsecond render"); err != nil {
		t.Fatalf("second Upsert: %v", err)
	}

	if len(fp.comments) != 1 {
		t.Fatalf("got %d comments after two runs, want 1 (stacked instead of updated): %+v", len(fp.comments), fp.comments)
	}
	if fp.createCalls != 1 || fp.updateCalls != 1 {
		t.Fatalf("got create=%d update=%d, want create=1 update=1", fp.createCalls, fp.updateCalls)
	}
	if fp.comments[0].Body != commentMarker+"\nsecond render" {
		t.Fatalf("comment body was not updated: %q", fp.comments[0].Body)
	}
}

func TestUpsertIgnoresUnmarkedComments(t *testing.T) {
	fp := &fakeCommentPoster{comments: []postedComment{
		{ID: 1, Body: "an unrelated human comment"},
	}}
	if err := Upsert(context.Background(), fp, "o11y-one", "sdk", 42, commentMarker, commentMarker+"\nrendered"); err != nil {
		t.Fatalf("Upsert: %v", err)
	}
	if len(fp.comments) != 2 {
		t.Fatalf("got %d comments, want 2 (unrelated comment preserved, new one created): %+v", len(fp.comments), fp.comments)
	}
}
