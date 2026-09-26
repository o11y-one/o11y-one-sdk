// `@o11y-one/sdk/api` re-exports the whole generated surface.
//
// The check walks the generated package's dist and asserts every export of
// every *_pb module is reachable from api.js, so a newly generated module that
// nobody added to src/api.ts fails here instead of in a user's import.
import { strict as assert } from "node:assert";
import { readdirSync } from "node:fs";
import { createRequire } from "node:module";
import { dirname, join, relative } from "node:path";
import { test } from "node:test";

import { AgenticEvaluationService } from "@o11y-one/api-agentic/o11y_one/agentic/v1/evaluation_pb";

import * as api from "../dist/api.js";

const require = createRequire(import.meta.url);
// The generated package exports only "./*" -> dist, so resolve a module and
// walk up to dist/o11y_one rather than asking for its package.json.
const generatedRoot = join(
  dirname(require.resolve("@o11y-one/api-agentic/o11y_one/common/v1/common_pb")),
  "..",
  "..",
);

function generatedModules(dir) {
  return readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    const path = join(dir, entry.name);
    if (entry.isDirectory()) return generatedModules(path);
    return entry.name.endsWith("_pb.js") ? [path] : [];
  });
}

test("the api subpath re-exports the service descriptor by identity", () => {
  assert.equal(api.AgenticEvaluationService, AgenticEvaluationService);
  assert.equal(api.AgenticEvaluationService.typeName, "o11y_one.agentic.v1.AgenticEvaluationService");
});

test("every export of every generated module is reachable from the api subpath", async () => {
  const modules = generatedModules(generatedRoot);
  assert.ok(modules.length >= 5, `expected the agentic closure, found ${modules.length} modules`);
  for (const path of modules) {
    const generated = await import(path);
    for (const name of Object.keys(generated)) {
      assert.ok(name in api, `${relative(generatedRoot, path)} exports ${name}, api.ts does not`);
    }
  }
});
