import subprocess
import sys

from qacalc.cli import main


def test_add_basic(capsys):
    main(["add", "2", "3"])
    assert capsys.readouterr().out == "5\n"


def test_add_negative_numbers(capsys):
    main(["add", "-2", "3"])
    assert capsys.readouterr().out == "1\n"


def test_add_floats(capsys):
    main(["add", "2.5", "1.5"])
    assert capsys.readouterr().out == "4.0\n"


def test_subtract_basic(capsys):
    main(["subtract", "5", "3"])
    assert capsys.readouterr().out == "2\n"


def test_subtract_negative_numbers(capsys):
    main(["subtract", "-5", "-3"])
    assert capsys.readouterr().out == "-2\n"


def test_subtract_floats(capsys):
    main(["subtract", "5.5", "2.5"])
    assert capsys.readouterr().out == "3.0\n"


def test_module_entrypoint():
    result = subprocess.run(
        [sys.executable, "-m", "qacalc", "add", "2", "3"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "5"
