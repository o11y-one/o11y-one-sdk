"""pyfix's cases: 64 small Python modules, each with one function that breaks its docstring.

``python cases.py > pyfix.jsonl`` writes the dataset version's JSONL: each line's prompt
carries its module, and its ``verifier_inputs`` the hidden tests, which Loop hands only
the verifier, at /verifier/case/tests.json.
"""

from __future__ import annotations

import json
import random

# The pool every case draws five functions from, each correct as written here.
SOURCE = '''def clamp(x, lo, hi):
    """x, limited to lo..hi."""
    return max(lo, min(x, hi))


def mean(xs):
    """The average of xs, or 0.0 when xs is empty."""
    return sum(xs) / len(xs) if xs else 0.0


def is_palindrome(text):
    """Whether text reads the same backwards, ignoring case and all but letters and digits."""
    kept = [c.lower() for c in text if c.isalnum()]
    return kept == kept[::-1]


def fizzbuzz(n):
    """FizzBuzz for multiples of 15, Fizz of 3, Buzz of 5, else n."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def count_words(text):
    """How often each whitespace-separated word occurs in text."""
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def running_max(xs):
    """The largest value so far at each position of xs."""
    out = []
    for x in xs:
        out.append(max(out[-1], x) if out else x)
    return out


def chunk(xs, n):
    """xs as consecutive lists of n, the last one shorter if need be."""
    return [xs[i : i + n] for i in range(0, len(xs), n)]


def dedupe(xs):
    """xs without repeats, each value where it first occurs."""
    return list(dict.fromkeys(xs))
'''
FUNCTIONS = {
    part.split("(")[0].removeprefix("def "): part for part in SOURCE.strip().split("\n\n\n")
}

# Each function's one bug, as (old, new), and the calls its hidden tests make.
BUGS = {
    "clamp": ("max(lo, min(x, hi))", "min(lo, max(x, hi))"),
    "mean": ("sum(xs) / len(xs)", "sum(xs) / (len(xs) + 1)"),
    "is_palindrome": ("c.lower() for c", "c for c"),
    "fizzbuzz": ("n % 15 == 0", "n % 15 == 1"),
    "count_words": ("text.split()", 'text.split(" ")'),
    "running_max": ("max(out[-1], x) if out else x", "max(out[-1] if out else 0, x)"),
    "chunk": ("range(0, len(xs), n)", "range(0, len(xs) - n, n)"),
    "dedupe": ("list(dict.fromkeys(xs))", "sorted(set(xs))"),
}
CALLS = {
    "clamp": [[5, 0, 10], [-3, 0, 10], [42, 0, 10]],
    "mean": [[[1, 2, 3]], [[4]], [[]]],
    "is_palindrome": [["Racecar"], ["ab"], ["A man, a plan, a canal: Panama"]],
    "fizzbuzz": [[15], [9], [10], [7]],
    "count_words": [["a b  a"], ["x"], [""]],
    "running_max": [[[-3, -1, -2]], [[1, 3, 2]]],
    "chunk": [[[1, 2, 3, 4, 5], 2], [[1, 2], 2], [[], 3]],
    "dedupe": [[[3, 1, 3, 2]], [[1, 1]], [[2, 1]]],
}

PROMPT = """The Python module below has one bug: one function does not do what its docstring says.
Fix it, and write the whole fixed module to /work/mod.py. You can run commands to check it.

```python
{module}```"""


def generate(count: int = 64) -> list[dict]:
    """``count`` distinct cases: five of the pool's functions each, one of them broken."""
    cases, seen, seed = [], set(), 0
    while len(cases) < count:
        rng = random.Random(seed)
        seed += 1
        names = rng.sample(sorted(FUNCTIONS), 5)
        broken = rng.choice(names)
        if (tuple(names), broken) in seen:
            continue
        seen.add((tuple(names), broken))
        namespace: dict = {}
        fixed = "\n\n\n".join(FUNCTIONS[name] for name in names) + "\n"
        exec(fixed, namespace)
        tests = [
            [name, args, repr(namespace[name](*args))] for name in names for args in CALLS[name]
        ]
        module = fixed.replace(*BUGS[broken])
        cases.append({"module": module, "fixed": fixed, "tests": tests})
    return cases


def dataset_lines(cases: list[dict]) -> list[str]:
    return [
        json.dumps(
            {
                "input_payload": {
                    "messages": [{"role": "user", "content": PROMPT.format(module=case["module"])}]
                },
                "verifier_inputs": {
                    "files": [
                        {"path": "tests.json", "content": json.dumps({"tests": case["tests"]})}
                    ]
                },
            }
        )
        for case in cases
    ]


if __name__ == "__main__":
    print("\n".join(dataset_lines(generate())))
