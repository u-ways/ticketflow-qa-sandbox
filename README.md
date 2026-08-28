# qacalc

A minimal, typed calculator package for Python, exposing `add`, `subtract`,
`multiply`, and `divide` — as both an importable library and a command-line
tool.

## Installation

`qacalc` isn't published to PyPI; install it directly from this repository.

```bash
git clone https://github.com/u-ways/ticketflow-qa-sandbox.git
cd ticketflow-qa-sandbox
pip install .
```

For development (adds `pytest` and installs in editable mode so source
changes are picked up immediately):

```bash
pip install -e ".[test]"
```

Requires Python 3.9+.

## Python API

Every function accepts `int` or `float` and returns a number:

```pycon
>>> import qacalc
>>> qacalc.add(2, 3)
5
>>> qacalc.subtract(5, 3)
2
>>> qacalc.multiply(4, 3)
12
>>> qacalc.divide(6, 3)
2.0
```

`divide` always returns a `float`, even for evenly-divisible inputs. Dividing
by zero raises `ZeroDivisionError` with a descriptive message instead of
Python's default one:

```pycon
>>> qacalc.divide(5, 0)
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero: 5 / 0
```

## CLI usage

Installing the package also installs a `qacalc` console script
(`python -m qacalc` works identically):

```console
$ qacalc add 2 3
5
$ qacalc subtract 10 4
6
$ qacalc multiply 6 7
42
$ qacalc divide 6 3
2
```

Whole-number results — including from `divide`, which is always a float
internally — print without a trailing `.0`. Non-whole results print in full:

```console
$ qacalc divide 1 3
0.3333333333333333
```

Dividing by zero prints an error to stderr and exits with status `1`,
instead of a raw Python traceback:

```console
$ qacalc divide 5 0
error: division by zero: 5 / 0
$ echo $?
1
```

## License

MIT — see [LICENSE](LICENSE).
