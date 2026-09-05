/**
 * `@o11y-one/sdk` — hand-written client layer over the generated `@o11y-one/api`.
 *
 * Three things live here and nothing else:
 *   - transport construction (client.ts)
 *   - credential injection and its local validation (auth.ts)
 *   - the failure taxonomy an SDK exists to render (errors.ts)
 *
 * Service methods are NOT re-exported or wrapped. Import the descriptor you
 * need from `@o11y-one/api` and hand it to `O11yClient.service()`.
 */
export {
  O11yClient,
  createTransport,
  credentialInterceptor,
  type ClientOptions,
} from "./client.js";

export {
  assertLooksLikeMachineCredential,
  CREDENTIAL_HEADER,
  CREDENTIAL_MAX_LEN,
  MACHINE_CREDENTIAL_PREFIX,
  ORG_ID_HEADER,
  TENANT_ID_HEADER,
  type MachineCredential,
} from "./auth.js";

export {
  classify,
  MACHINE_SCOPES,
  type ClassifiedFailure,
  type FailureDisposition,
  type MachineScope,
} from "./errors.js";
