/**
 * Transport construction and credential injection.
 *
 * Scope discipline: this file builds a transport and attaches headers. It does
 * NOT wrap RPCs in convenience methods. `@o11y-one/api` already exposes every
 * service descriptor, and connect-es v2 turns a descriptor into a typed client
 * with `createClient(Desc, transport)`. A hand-written facade over 29 services
 * would be a second API surface to keep in sync with the proto, and it would
 * rot the first time a field is added upstream.
 */
import { createClient, type Client, type Interceptor, type Transport } from "@connectrpc/connect";
import {
  createConnectTransport,
  type ConnectTransportOptions,
} from "@connectrpc/connect-web";
import type { DescService } from "@bufbuild/protobuf";

import {
  assertLooksLikeMachineCredential,
  CREDENTIAL_HEADER,
  ORG_ID_HEADER,
  TENANT_ID_HEADER,
} from "./auth.js";

export interface ClientOptions {
  /**
   * Base URL of the O11y One Connect endpoint, e.g. `https://api.o11y.one`.
   * No trailing path — connect-es appends `/<package>.<Service>/<Method>`.
   */
  baseUrl: string;

  /**
   * Machine credential, `o11y_mach.<selector>.<secret>`.
   *
   * Optional so that unauthenticated surfaces (capability discovery, health)
   * can be reached without one. Every authenticated call will fail with
   * UNAUTHENTICATED if it is absent — see `classify()` in errors.ts.
   */
  credential?: string;

  /** Org to scope the call to (`x-o11y-org-id`). */
  orgId?: string;

  /** Tenant to scope the call to (`x-o11y-tenant-id`). */
  tenantId?: string;

  /** Extra interceptors, applied after the credential interceptor. */
  interceptors?: Interceptor[];

  /**
   * Override the fetch implementation. Defaults to the ambient `globalThis.fetch`;
   * Node 26 has one. This exists for tests and for runtimes that wrap fetch.
   *
   * The type is borrowed from connect-web rather than spelled
   * `typeof globalThis.fetch`, which would force the DOM lib into this package's
   * compilation for the sake of one type and drag every DOM global in with it.
   */
  fetch?: ConnectTransportOptions["fetch"];
}

/**
 * An interceptor that stamps the credential and scoping headers onto every
 * outbound request.
 *
 * This is THE auth-injection point for the TypeScript SDK. Everything about the
 * shape it injects is settled (see auth.ts). What is NOT settled, and is the
 * one open dependency this package has on the backend:
 *
 * TODO(w50a-auth-shape / lane 50A): the machine-principal management surface —
 *   CreateMachinePrincipal, ListMachinePrincipals, CreateMachineCredential,
 *   RevokeMachineCredential, RevokeMachinePrincipal, GetCallerPrincipal
 *   — does not exist in the proto snapshot at PROTO_PIN (fb8f5098). auth.proto
 *   there carries only AuthFoundationService.ListAuthMethods. The RPC NAMES are
 *   held by 50A and will not move, so when lane A lands them:
 *     1. bump PROTO_PIN and run tools/sync-proto.sh,
 *     2. add `O11yClient.whoami()` over GetCallerPrincipal — the introspection
 *        call that answers "is my credential valid, and which scopes does it
 *        carry?" BEFORE a run, which is what makes `o11y-eval doctor` possible
 *        and what turns an UNAUTHENTICATED at minute 40 into an error at
 *        minute 0.
 *   Nothing else in this file changes: the header, the encoding and the error
 *   taxonomy are already the final ones.
 */
export function credentialInterceptor(options: {
  credential?: string;
  orgId?: string;
  tenantId?: string;
}): Interceptor {
  const credential = options.credential
    ? assertLooksLikeMachineCredential(options.credential)
    : undefined;

  return (next) => async (req) => {
    if (credential !== undefined) {
      req.header.set(CREDENTIAL_HEADER, credential);
    }
    if (options.orgId !== undefined) {
      req.header.set(ORG_ID_HEADER, options.orgId);
    }
    if (options.tenantId !== undefined) {
      req.header.set(TENANT_ID_HEADER, options.tenantId);
    }
    return await next(req);
  };
}

/**
 * Build a Connect transport with the credential interceptor installed.
 *
 * Protocol note: Connect over HTTP, not gRPC. It is the protocol o11y-web
 * already speaks and the one that survives proxies and CI egress rules without
 * HTTP/2 prior knowledge. `createConnectTransport` from `@connectrpc/connect-web`
 * works in browsers, in Node 26 (whose global fetch is sufficient), and in
 * Workers; `@connectrpc/connect-node` is a dependency only for callers who need
 * the Node-specific HTTP/2 transport and reach for it themselves.
 */
export function createTransport(options: ClientOptions): Transport {
  return createConnectTransport({
    baseUrl: options.baseUrl,
    // Binary wire format: smaller, and it round-trips proto3 field presence
    // without the JSON mapping's ambiguities.
    useBinaryFormat: true,
    interceptors: [
      credentialInterceptor({
        credential: options.credential,
        orgId: options.orgId,
        tenantId: options.tenantId,
      }),
      ...(options.interceptors ?? []),
    ],
    ...(options.fetch ? { fetch: options.fetch } : {}),
  });
}

/**
 * A thin holder for the transport, so callers construct credentials once and
 * mint typed clients per service.
 *
 * ```ts
 * import { O11yClient } from "@o11y-one/sdk";
 * import { BillingUsageService } from "@o11y-one/api/o11y_one/billing/v1/billing_pb";
 *
 * const o11y = new O11yClient({ baseUrl, credential: process.env.O11Y_API_KEY });
 * const billing = o11y.service(BillingUsageService);
 * const summary = await billing.getUsageSummary({});
 * ```
 */
export class O11yClient {
  readonly transport: Transport;

  constructor(options: ClientOptions) {
    this.transport = createTransport(options);
  }

  /** Mint a typed client for any generated service descriptor. */
  service<T extends DescService>(desc: T): Client<T> {
    return createClient(desc, this.transport);
  }
}
