import subprocess
import sys

from qacalc.cli import main


def test_add_via_main(capsys):
    assert main(["add", "2", "3"]) == 0
    assert capsys.readouterr().out.strip() == "5"


def test_subtract_via_main(capsys):
    assert main(["subtract", "5", "3"]) == 0
    assert capsys.readouterr().out.strip() == "2"


def test_subtract_negative_result_via_main(capsys):
    assert main(["subtract", "2", "5"]) == 0
    assert capsys.readouterr().out.strip() == "-3"


def test_add_negative_operand_via_main(capsys):
    assert main(["add", "-2", "-3"]) == 0
    assert capsys.readouterr().out.strip() == "-5"


def test_add_via_subprocess():
    result = subprocess.run(
        [sys.executable, "-m", "qacalc", "add", "2", "3"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "5"


def test_subtract_via_subprocess():
    result = subprocess.run(
        [sys.executable, "-m", "qacalc", "subtract", "5", "3"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "2"
