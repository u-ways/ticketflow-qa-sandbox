from __future__ import annotations

import subprocess
import sys


def run_cli(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "qacalc", *args],
        capture_output=True,
        text=True,
    )


def test_cli_add():
    result = run_cli("add", "2", "3")
    assert result.returncode == 0
    assert result.stdout == "5\n"


def test_cli_subtract():
    result = run_cli("subtract", "5", "3")
    assert result.returncode == 0
    assert result.stdout == "2\n"


def test_cli_multiply():
    result = run_cli("multiply", "4", "3")
    assert result.returncode == 0
    assert result.stdout == "12\n"


def test_cli_divide():
    result = run_cli("divide", "10", "2")
    assert result.returncode == 0
    assert result.stdout == "5\n"


def test_cli_divide_whole_number_result_has_no_trailing_zero():
    result = run_cli("divide", "6", "3")
    assert result.returncode == 0
    assert result.stdout == "2\n"


def test_cli_divide_non_whole_number_result_keeps_fraction():
    result = run_cli("divide", "5", "2")
    assert result.returncode == 0
    assert result.stdout == "2.5\n"


def test_cli_negative_operand():
    result = run_cli("add", "-2", "3")
    assert result.returncode == 0
    assert result.stdout == "1\n"


def test_cli_divide_by_zero_exits_nonzero_without_traceback():
    result = run_cli("divide", "1", "0")
    assert result.returncode != 0
    assert "Traceback" not in result.stderr
    assert result.stdout == ""
