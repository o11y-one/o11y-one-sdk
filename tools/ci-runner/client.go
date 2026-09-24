package main

import (
	"context"
	"net/http"
	"time"

	"connectrpc.com/connect"

	agenticv1connect "github.com/o11y-one/o11y-one-sdk/gen/go/o11y_one/agentic/v1/agenticv1connect"
)

// Header names the platform reads off every request. The credential rides in
// x-o11y-key; org and tenant scope the call. These are the same headers the
// hand-written SDKs send (packages/sdk-ts, packages/sdk-py).
const (
	headerKey    = "x-o11y-key"
	headerOrgID  = "x-o11y-org-id"
	headerTenant = "x-o11y-tenant-id"
)

// apiClients is the connect client this runner drives. The evaluation service
// owns run launch, run status, platform annotations, and the run overview the
// verdict is read off.
type apiClients struct {
	eval agenticv1connect.AgenticEvaluationServiceClient
}

// newClients builds the connect clients for a command.
//
// The credential is injected by an interceptor rather than baked into each call
// site, so there is exactly one place that touches it and exactly zero places
// that log it. The interceptor sets headers on outbound requests only; it never
// reads them back, never prints them, and never returns them in an error.
func newClients(common *commonFlags, cred string) *apiClients {
	httpClient := &http.Client{
		// A generous per-request ceiling. The overall command deadline is the
		// real bound (see commonFlags.timeout); this only stops a single wedged
		// socket from outliving everything.
		Timeout: 0, // no per-client timeout: deadlines come from context.
	}

	auth := connect.UnaryInterceptorFunc(func(next connect.UnaryFunc) connect.UnaryFunc {
		return func(ctx context.Context, req connect.AnyRequest) (connect.AnyResponse, error) {
			// Only stamp outbound client requests; a client interceptor never
			// sees server-side requests, but guard anyway.
			if req.Spec().IsClient {
				h := req.Header()
				h.Set(headerKey, cred)
				if common.orgID != "" {
					h.Set(headerOrgID, common.orgID)
				}
				if common.tenantID != "" {
					h.Set(headerTenant, common.tenantID)
				}
			}
			return next(ctx, req)
		}
	})

	// The API serves gRPC and gRPC-web, not the Connect protocol; gRPC-web
	// needs no HTTP/2 prior knowledge.
	opts := []connect.ClientOption{connect.WithGRPCWeb(), connect.WithInterceptors(auth)}

	return &apiClients{
		eval: agenticv1connect.NewAgenticEvaluationServiceClient(httpClient, common.baseURL, opts...),
	}
}

// commandContext derives the command-scoped context and its cancel func from the
// common --timeout. Every RPC and every wait loop hangs off this deadline, so a
// stuck platform can never turn into a stuck pipeline.
func (c *commonFlags) commandContext() (context.Context, context.CancelFunc) {
	if c.timeout <= 0 {
		return context.WithCancel(context.Background())
	}
	return context.WithTimeout(context.Background(), c.timeout)
}

// nowUTC is the runner's clock, indirected so tests can pin it.
var nowUTC = func() time.Time { return time.Now().UTC() }
