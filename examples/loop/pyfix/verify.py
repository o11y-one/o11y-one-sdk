"""pyfix's verifier: grades /work/mod.py against the case's hidden tests.

Loop hands it the case's tests at /verifier/case/tests.json and the episode's /work.
It writes /logs/verifier/result.json: ``tests_passed`` (the share of tests passed,
the primary reward) and ``all_passed``. It grades only as root (the spec's default
``run_as_uid``): the policy's module runs in a subprocess as nobody, after the expected
answers are gone from disk, so it can reach neither them nor this process.
"""

from __future__ import annotations

import json
import os
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

TIMEOUT_S = 20
MODULE_MAX_BYTES = 1 << 20
NOBODY = 65534

# Runs the module, then each call; answers each result's repr, or the exception it raised.
RUNNER = """
import json, sys
job = json.load(sys.stdin)
namespace = {"__name__": "mod"}
exec(compile(job["source"], "mod.py", "exec"), namespace)
out = []
for name, args in job["calls"]:
    try:
        out.append(repr(namespace[name](*args)))
    except BaseException as error:
        out.append("raised " + type(error).__name__)
print("\\n" + json.dumps(out))
"""


def grade(source: str, tests: list, user: int | None = NOBODY) -> int:
    """How many of ``tests`` ([function, args, expected repr]) the module passes, run as
    ``user`` (``None``: as this process, for tests only)."""
    as_user = {} if user is None else {"user": user, "group": user, "extra_groups": []}
    job = json.dumps({"source": source, "calls": [[name, args] for name, args, _ in tests]})
    try:
        run = subprocess.run(
            [sys.executable, "-I", "-c", RUNNER],
            input=job,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_S,
            cwd="/",
            env={},
            **as_user,
        )
        got = json.loads(run.stdout.splitlines()[-1])
    except (subprocess.TimeoutExpired, ValueError, IndexError):
        return 0
    return sum(answer == expected for answer, (_, _, expected) in zip(got, tests, strict=False))


def read_module(path: Path) -> str:
    """The module's text: a regular file, never through a link, at most 1 MiB."""
    try:
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    except OSError:
        return ""
    with os.fdopen(fd, "rb") as file:
        if not stat.S_ISREG(os.fstat(file.fileno()).st_mode):
            return ""
        return file.read(MODULE_MAX_BYTES).decode(errors="replace")


def main(
    work: Path = Path("/work"),
    case: Path = Path("/verifier/case"),
    logs: Path = Path("/logs/verifier"),
    user: int | None = NOBODY,
) -> None:
    if os.geteuid() != 0:
        # The policy's code would share this uid: it could read the answers from this
        # process's memory, or outlive it and rewrite result.json.
        raise PermissionError("pyfix's verifier grades only as root: keep run_as_uid 0")
    tests_file = case / "tests.json"
    tests = json.loads(tests_file.read_text())["tests"]
    tests_file.unlink()  # before any of the policy's code runs
    source = read_module(work / "mod.py")
    passed = grade(source, tests, user) if source else 0
    rewards = {"tests_passed": passed / len(tests), "all_passed": float(passed == len(tests))}
    verdict = "pass" if passed == len(tests) else "partial" if passed else "fail"
    # A fresh file, renamed over the path: nothing the module left there is written through.
    fd, partial = tempfile.mkstemp(dir=logs)
    with os.fdopen(fd, "w") as file:
        json.dump({"rewards": rewards, "verdict": verdict}, file)
    os.chmod(partial, 0o644)
    os.replace(partial, logs / "result.json")


if __name__ == "__main__":
    main()
