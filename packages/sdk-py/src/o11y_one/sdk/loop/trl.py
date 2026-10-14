"""TRL's ``GRPOTrainer`` on a Loop run, through its own public hooks::

    GRPOTrainer(
        model, args=args, train_dataset=dataset,
        environment_factory=LoopEnvironment,
        reward_funcs=[loop_reward],
        callbacks=[LoopCallback()],
    )

Each rollout is a :class:`LoopEnvironment`; its tools run in Loop's VM, and its
reward is the Loop verifier's primary reward, which :func:`loop_reward` closes
the batch's rollouts for, all at once. Our failures (``INFRASTRUCTURE``) and
cancellations score ``None``, which TRL leaves out of the advantages; a task's
or verifier's failure keeps its value. Needs the ``trl`` extra:
``pip install 'o11y-one[trl]'``.
"""

from __future__ import annotations

import itertools
import uuid
from collections import defaultdict
from concurrent.futures import Future, ThreadPoolExecutor
from types import SimpleNamespace
from typing import Any

try:
    import trl
    from transformers import TrainerCallback
except ModuleNotFoundError as error:
    raise ImportError(
        "o11y_one.sdk.loop.trl needs the trl extra: pip install 'o11y-one[trl]'"
    ) from error

from . import _SDK_VERSION, LoopClient, _core

__all__ = ["LoopCallback", "LoopEnvironment", "loop_reward"]

_GROUPS = uuid.uuid5(uuid.NAMESPACE_URL, "https://o11y.one/loop/trl/group")

# What LoopCallback learns of the trainer, for this process's environments.
# ponytail: one trainer per process; two GRPOTrainers in one process would share it.
_trainer = SimpleNamespace(
    pool=None,
    group_size=0,
    step=0,
    total_steps=0,
    experiment="",
    indices=defaultdict(itertools.count),
)


class LoopCallback(TrainerCallback):
    """Tells this process's :class:`LoopEnvironment` instances the group size,
    the training step and the run's name, and sizes the pool their resets and
    closes run on to the generation batch."""

    def on_train_begin(self, args: Any, state: Any, control: Any, **kwargs: Any) -> None:
        if _trainer.pool is None:
            _trainer.pool = ThreadPoolExecutor(args.generation_batch_size, "o11y-loop")
        _trainer.group_size = args.num_generations
        _trainer.total_steps = state.max_steps
        _trainer.experiment = args.run_name or ""

    def on_step_begin(self, args: Any, state: Any, control: Any, **kwargs: Any) -> None:
        _trainer.step = state.global_step
        _trainer.indices.clear()


class LoopEnvironment:
    """One rollout at a time of the run ``O11Y_RUN``, with the key
    ``O11Y_API_KEY``; ``client`` arguments go to :class:`LoopClient`, e.g.
    ``functools.partial(LoopEnvironment, base_url=...)``.

    TRL calls ``reset`` serially over the whole batch, so it only starts the
    rollout and answers at once; the first tool call waits for it.
    """

    def __init__(self, **client: Any) -> None:
        self._client = LoopClient(
            adapter=__name__,
            adapter_version=_SDK_VERSION,
            framework_version=trl.__version__,
            **client,
        )
        self._started: Future | None = None

    def reset(self, **row: Any) -> None:
        if not _trainer.group_size:
            raise RuntimeError("LoopEnvironment needs GRPOTrainer(callbacks=[LoopCallback()])")
        case = row.get("loop_case_revision_id")
        # Content-derived, so every process names a group alike.
        task = case or repr(row.get("prompt"))
        group = str(uuid.uuid5(_GROUPS, f"{self._client._run}/{_trainer.step}/{task}"))
        fields = {
            "group_id": group,
            "group_index": next(_trainer.indices[group]) % _trainer.group_size,
            "group_size": _trainer.group_size,
            "trainer_step": _trainer.step,
            "trainer_total_steps": _trainer.total_steps,
            "experiment_name": _trainer.experiment,
        }
        if case:
            fields["case_revision_id"] = case
        self._started = _trainer.pool.submit(self._client.reset, **fields)

    def shell(self, command: str) -> str:
        """Runs a shell script in the task's environment and shows its exit code and output.

        Args:
            command: The script, run by /bin/sh -c.
        """
        return self._step("shell", command=command)

    def read_file(self, path: str) -> str:
        """Reads a file in the task's environment.

        Args:
            path: The file's absolute path.
        """
        return self._step("read_file", path=path)

    def write_file(self, path: str, content: str) -> str:
        """Writes a file in the task's environment, replacing any file at that path.

        Args:
            path: The file's absolute path.
            content: The file's new content.
        """
        return self._step("write_file", path=path, content=content)

    def _step(self, name: str, **arguments: str) -> str:
        # A refused reset raises here, into the model's context; _close raises it again.
        self._started.result()
        (result,) = self._client.step([_core.to_call(name, arguments)]).results
        return _core.render(result)

    def _close(self) -> float | None:
        self._started.result()
        return _core.reward(self._client.close())


def loop_reward(environments: list[LoopEnvironment], **_: Any) -> list[float | None]:
    """TRL's reward function: closes the batch's rollouts all at once and
    answers each one's primary reward, in order. A reset Loop refused raises
    its :class:`~o11y_one.sdk.loop.RolloutRefused` here, so training stops on
    the code rather than scoring rollouts that never ran."""
    return list(_trainer.pool.map(LoopEnvironment._close, environments))
