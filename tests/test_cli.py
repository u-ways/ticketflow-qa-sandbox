import subprocess
import sys

import pytest

from qacalc.cli import main


def run_cli(*args):
    return subprocess.run(
        [sys.executable, "-m", "qacalc", *args],
        capture_output=True,
        text=True,
    )


def test_add_integers_via_subprocess():
    result = run_cli("add", "2", "3")
    assert result.returncode == 0
    assert result.stdout.strip() == "5"


def test_subtract_integers_via_subprocess():
    result = run_cli("subtract", "5", "3")
    assert result.returncode == 0
    assert result.stdout.strip() == "2"


def test_add_floats_via_subprocess():
    result = run_cli("add", "2.5", "3")
    assert result.returncode == 0
    assert result.stdout.strip() == "5.5"


def test_subtract_floats_via_subprocess():
    result = run_cli("subtract", "5.5", "2.5")
    assert result.returncode == 0
    assert result.stdout.strip() == "3.0"


def test_add_negative_numbers_via_subprocess():
    result = run_cli("add", "-2", "-3")
    assert result.returncode == 0
    assert result.stdout.strip() == "-5"


def test_subtract_negative_numbers_via_subprocess():
    result = run_cli("subtract", "-5", "-3")
    assert result.returncode == 0
    assert result.stdout.strip() == "-2"


def test_unknown_command_via_subprocess():
    result = run_cli("bogus", "1", "2")
    assert result.returncode != 0
    assert "invalid choice" in result.stderr


def test_invalid_number_via_subprocess():
    result = run_cli("add", "2", "x")
    assert result.returncode != 0
    assert "invalid number:" in result.stderr


def test_missing_argument_via_subprocess():
    result = run_cli("add", "2")
    assert result.returncode != 0
    assert "required" in result.stderr


def test_add_via_main(capsys):
    exit_code = main(["add", "2", "3"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "5"


def test_subtract_via_main(capsys):
    exit_code = main(["subtract", "5", "3"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "2"


def test_add_floats_via_main(capsys):
    exit_code = main(["add", "2.5", "3"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "5.5"


def test_add_negative_numbers_via_main(capsys):
    exit_code = main(["add", "-2", "-3"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "-5"


def test_unknown_command_via_main_raises_system_exit():
    with pytest.raises(SystemExit) as exc_info:
        main(["bogus", "1", "2"])
    assert exc_info.value.code != 0
