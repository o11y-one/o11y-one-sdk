"""examples/loop/pyfix: its case generator and its verifier, run here against temp roots."""

from __future__ import annotations

import importlib.util
import json
import subprocess
from pathlib import Path

import pytest
from google.protobuf.json_format import Parse
from o11y_one.agentic.v1.environment_pb2 import LoopEnvironmentSpecV1

PYFIX = Path(__file__).resolve().parents[3] / "examples/loop/pyfix"


def load(name: str):
    spec = importlib.util.spec_from_file_location(f"pyfix_{name}", PYFIX / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cases, verify = load("cases"), load("verify")
CASES = cases.generate()


@pytest.fixture(autouse=True)
def root(monkeypatch: pytest.MonkeyPatch) -> None:
    """The verifier runs as root; here the policy's code then runs as this test's user."""
    monkeypatch.setattr(verify.os, "geteuid", lambda: 0)


def verified(tmp_path: Path, source: str | None, tests: list) -> dict:
    """The verifier's result.json for /work/mod.py = ``source`` (absent when None)."""
    work, case, logs = (tmp_path / name for name in ("work", "case", "logs"))
    for path in (work, case, logs):
        path.mkdir(parents=True, exist_ok=True)
    (case / "tests.json").write_text(json.dumps({"tests": tests}))
    if source is not None:
        (work / "mod.py").write_text(source)
    verify.main(work=work, case=case, logs=logs, user=None)
    assert not (case / "tests.json").exists(), "the expected answers outlive the policy's code"
    return json.loads((logs / "result.json").read_text())


def test_64_distinct_cases_each_with_one_bug_its_tests_catch() -> None:
    assert len(CASES) == 64
    assert len({case["module"] for case in CASES}) == 64
    for case in CASES:
        passed = verify.grade(case["module"], case["tests"], user=None)
        assert passed < len(case["tests"]), case["module"]
        assert verify.grade(case["fixed"], case["tests"], user=None) == len(case["tests"])


def test_each_dataset_line_carries_the_module_and_its_hidden_tests_within_bounds() -> None:
    for case, line in zip(CASES, cases.dataset_lines(CASES), strict=True):
        row = json.loads(line)
        (message,) = row["input_payload"]["messages"]
        assert case["module"] in message["content"] and "/work/mod.py" in message["content"]
        (file,) = row["verifier_inputs"]["files"]
        assert file["path"] == "tests.json"
        assert json.loads(file["content"]) == {"tests": case["tests"]}
        assert len(file["content"].encode()) <= 256 * 1024
        assert json.dumps(case["fixed"])[1:-1] not in line


def test_the_fixed_module_passes_and_the_buggy_one_does_not(tmp_path: Path) -> None:
    case = CASES[7]
    fixed = verified(tmp_path / "fixed", case["fixed"], case["tests"])
    assert fixed == {"rewards": {"tests_passed": 1.0, "all_passed": 1.0}, "verdict": "pass"}
    buggy = verified(tmp_path / "buggy", case["module"], case["tests"])
    assert 0 < buggy["rewards"]["tests_passed"] < 1
    assert (buggy["rewards"]["all_passed"], buggy["verdict"]) == (0.0, "partial")


def test_no_module_scores_zero(tmp_path: Path) -> None:
    result = verified(tmp_path, None, CASES[0]["tests"])
    assert result == {"rewards": {"tests_passed": 0.0, "all_passed": 0.0}, "verdict": "fail"}


@pytest.mark.parametrize(
    "source",
    ["raise SystemExit(3)", "import os\nos._exit(0)", "while True:\n    pass"],
    ids=["raises", "exits", "loops"],
)
def test_a_module_that_crashes_exits_or_hangs_scores_zero(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, source: str
) -> None:
    monkeypatch.setattr(verify, "TIMEOUT_S", 2)
    result = verified(tmp_path, source, CASES[0]["tests"])
    assert result["rewards"] == {"tests_passed": 0.0, "all_passed": 0.0}


def test_a_module_reaching_outside_work_gains_nothing(tmp_path: Path) -> None:
    case = CASES[3]
    logs, tests_file = tmp_path / "logs", tmp_path / "case" / "tests.json"
    # Reads the expected answers to echo them back, and forges a perfect result.
    cheat = f"""
import json
try:
    EXPECTED = {{(n, repr(a)): e for n, a, e in json.load(open({str(tests_file)!r}))["tests"]}}
except OSError:
    EXPECTED = {{}}
for name in {{n for n, _ in EXPECTED}}:
    globals()[name] = lambda *args, n=name: eval(EXPECTED[(n, repr(list(args)))])
import os
FORGED = '{{"rewards": {{"tests_passed": 1, "all_passed": 1}}}}'
open({str(logs / "forged.json")!r}, "w").write(FORGED)
os.symlink({str(logs / "forged.json")!r}, {str(logs / "result.json")!r})
"""
    result = verified(tmp_path, case["module"] + cheat, case["tests"])
    assert result["rewards"]["all_passed"] == 0.0
    assert not (logs / "result.json").is_symlink()


def test_a_linked_module_is_no_module(tmp_path: Path) -> None:
    elsewhere = tmp_path / "elsewhere.py"
    elsewhere.write_text(CASES[0]["fixed"])
    (tmp_path / "work").mkdir()
    (tmp_path / "work" / "mod.py").symlink_to(elsewhere)
    assert verified(tmp_path, None, CASES[0]["tests"])["rewards"]["tests_passed"] == 0.0


def test_a_verifier_not_running_as_root_refuses_to_grade(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(verify.os, "geteuid", lambda: 1000)
    (tmp_path / "case").mkdir()
    (tmp_path / "case" / "tests.json").write_text(json.dumps({"tests": CASES[0]["tests"]}))
    with pytest.raises(PermissionError, match="only as root"):
        verify.main(work=tmp_path, case=tmp_path / "case", logs=tmp_path, user=None)
    assert not (tmp_path / "result.json").exists()


def test_the_policys_code_runs_as_nobody(monkeypatch: pytest.MonkeyPatch) -> None:
    seen: dict = {}

    def run(*args, **kwargs):
        seen.update(kwargs)
        raise subprocess.TimeoutExpired(args[0], 0)

    monkeypatch.setattr(verify.subprocess, "run", run)
    assert verify.grade("x = 1", CASES[0]["tests"]) == 0
    assert (seen["user"], seen["group"], seen["extra_groups"]) == (65534, 65534, [])


def test_the_spec_is_a_loop_environment_spec_with_tests_passed_primary() -> None:
    spec = Parse((PYFIX / "spec.json").read_text(), LoopEnvironmentSpecV1())
    verifier = spec.verifier
    assert [reward.name for reward in verifier.rewards] == ["tests_passed", "all_passed"]
    assert list(verifier.final_state_paths) == ["/work"]
    assert list(verifier.argv) == ["python3", "-I", "/verifier/verify.py"]
