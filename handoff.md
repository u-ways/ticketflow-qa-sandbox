# Handoff: multiply and divide operations

## Files touched
- `src/qacalc/__init__.py` — added `multiply` and `divide`.
- `tests/test_operations.py` — added tests for both, including divide-by-zero.

## Interfaces introduced
- `qacalc.multiply(a: float, b: float) -> float`
- `qacalc.divide(a: float, b: float) -> float` — raises `ZeroDivisionError("division by zero: b must not be 0")` when `b == 0`.

## Decisions
- Mirrored the exact style of the existing `add`/`subtract` (same docstring format, blank-line spacing, type hints).
- `divide` checks `b == 0` explicitly and raises `ZeroDivisionError` with a custom message, rather than letting Python's native `a / b` raise its own (less descriptive) `ZeroDivisionError`, per the acceptance criteria's "clear message" requirement.
- Tests follow the existing `test_<op>_normal` / `_negative` / `_zero` naming convention; divide-by-zero test uses `pytest.raises(ZeroDivisionError)`.

## Deliberately not done
- No changes to `pyproject.toml`, `.gitignore`, or CI — nothing here needed them.
- No parametrized tests, no float-precision edge cases (e.g. divide producing non-terminating decimals) — matches the minimal style of the existing suite.

## Verification
- Installed in a scratch venv (`pip install -e ".[test]"`) and ran `pytest`: all 12 tests pass (6 pre-existing + 6 new). Scratch venv deleted afterward; no build artifacts left in the working tree (`git status` clean apart from the two edited files).

## Known gotchas
- None. This change is purely additive and self-contained within `src/qacalc/` and `tests/`.
