import subprocess
import sys

import pytest

from qacalc.cli import main


@pytest.mark.parametrize(
    ("command", "a", "b", "expected"),
    [
        ("add", "2", "3", "5"),
        ("add", "2.5", "2.5", "5"),
        ("subtract", "5", "3", "2"),
        ("subtract", "2", "5", "-3"),
        ("multiply", "4", "2.5", "10"),
        ("multiply", "3", "3", "9"),
        ("divide", "6", "3", "2"),
        ("divide", "5", "2", "2.5"),
        ("divide", "1", "3", str(1 / 3)),
    ],
)
def test_cli_subcommands(capsys, command, a, b, expected):
    exit_code = main([command, a, b])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == expected
    assert captured.err == ""


@pytest.mark.parametrize("zero", ["0", "0.0"])
def test_cli_divide_by_zero(capsys, zero):
    exit_code = main(["divide", "5", zero])

    captured = capsys.readouterr()
    b = int(zero) if zero == "0" else float(zero)
    assert exit_code == 1
    assert captured.out == ""
    assert captured.err == f"error: division by zero: 5 / {b}\n"


def test_cli_module_entrypoint_subprocess():
    result = subprocess.run(
        [sys.executable, "-m", "qacalc", "add", "2", "3"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert result.stdout.strip() == "5"
