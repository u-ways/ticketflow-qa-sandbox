"""Allow running qacalc as `python -m qacalc`."""

from __future__ import annotations

import sys

from qacalc.cli import main

if __name__ == "__main__":
    sys.exit(main())
