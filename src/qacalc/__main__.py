"""Allow running qacalc as `python -m qacalc`."""

from qacalc.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
