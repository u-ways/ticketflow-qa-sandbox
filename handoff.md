# Handoff: qacalc README

## Files touched
- `README.md` — new, repo root.

## Interfaces introduced
None — documentation only.

## Decisions
- Verified every claim by actually running code rather than reading source alone: fresh venv, `pip install -e ".[test]"`, executed each Python API call and each CLI command, captured real stdout/exit codes.
- Documented `add`, `subtract`, `multiply`, `divide` in the Python API section (all four exist in `qacalc/__init__.py`), but the CLI section only shows `add`/`subtract` and explicitly notes `multiply`/`divide` are **not** wired into `cli.py`'s `OPERATIONS` dict — confirmed by running `qacalc multiply 2 3`, which fails with `invalid choice`. Documenting the mismatch instead of glossing over it.
- `divide(6, 3)` example shows `2.0` (raw Python float, since the library returns a float via `print()`), distinct from the CLI's `format_result()` which would print `"2"` for a whole-number CLI result — kept both behaviors distinct and correct in their respective sections rather than conflating them.
- Divide-by-zero example shows the real traceback with the exact custom message `division by zero: b must not be 0` (manually raised, not Python's default `ZeroDivisionError` text).
- Install instructions say "not published to PyPI, install from source" since no PyPI/index config exists in `pyproject.toml` and only `pip install -e .` was verified to work.

## Deliberately not done
- No CLI examples for `multiply`/`divide` since they don't exist as CLI subcommands — adding them would be inaccurate.
- No badges, license, or contributing sections — nothing in the repo supports them and the acceptance criteria didn't ask for them.

## Verification
- Ran a dedicated verification pass (separate from drafting) that independently re-read the source and re-ran every example in the drafted README against a fresh venv install. Result: "NO ISSUES FOUND" — all examples match real output exactly.
- Full test suite also passes: `pytest -q` → 18 passed.

## Known gotchas
None. Committed as `3bea642` on `tf/ec85927ec6ee` and pushed to origin.
