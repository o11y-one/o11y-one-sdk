# loop-ref-pyfix

This is the reference task for the trainer adapters' GRPO runs. Each case is a small Python
module in which one function breaks its docstring. The policy writes the fixed module to
`/work/mod.py`. The verifier then runs that module against hidden tests, which only it ever sees.

| File | Role |
|---|---|
| `spec.json` | The environment version's spec (`LoopEnvironmentSpecV1`, proto JSON) |
| `verify.py` | The verifier bundle's one file, run as `python3 -I /verifier/verify.py` |
| `cases.py` | `python cases.py > pyfix.jsonl` writes the dataset version: 64 cases |

## Set up (a person, in the web)

1. **Environment** `loop-ref-pyfix`:
   - Source: the OCI image `docker.io/library/python`, pinned by the digest of `3.12-slim`.
     To find it, run `docker buildx imagetools inspect python:3.12-slim`.
   - Spec: `spec.json`.
   - Verifier bundle: `verify.py`.
   - Keep the verifier's default `run_as_uid`, 0. `verify.py` grades only as root, and runs
     the policy's code as `nobody`. Any other uid would share a uid with that code, which
     could then read the answers or rewrite the result. So `verify.py` refuses, and every
     reward scores its minimum.
2. **Dataset version:** upload `pyfix.jsonl`.
   - Each line's prompt carries its module.
   - Each line's `verifier_inputs` carries `tests.json`. Loop hands it to the verifier at
     `/verifier/case/tests.json`, and never to the episode.
3. **A run per framework:** group size 8, environment limit 64, and the spend cap you choose.

## Rewards

- `tests_passed` is the primary reward: the share of the module's hidden calls that return the
  right value.
- `all_passed` is 1 when every call does, and 0 otherwise.
- A task or verifier failure scores each reward at its minimum, 0.
- How the verifier treats the policy's code:
  - It reads the expected answers, then deletes them from disk.
  - It runs the module in a subprocess: isolated, with an empty environment, under a 20 s
    timeout, and as `nobody` when it runs as root.
  - It writes `result.json` as a fresh file, renamed into place.
  - A missing or linked `/work/mod.py`, or a module that crashes, exits or hangs, scores 0.
