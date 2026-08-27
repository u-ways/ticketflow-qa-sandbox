# qacalc

A minimal calculator package for Python, providing basic arithmetic
operations through both a Python API and a command-line interface.

## Installation

qacalc requires Python 3.9 or later. Install it from a checkout of this
repository in editable mode:

```bash
pip install -e .
```

This also installs the `qacalc` console script.

## Python API

qacalc exposes four arithmetic operations: `add`, `subtract`, `multiply`,
and `divide`. Each accepts two `int` or `float` arguments and returns their
result.

```python
import qacalc

qacalc.add(2, 3)       # 5
qacalc.subtract(5, 2)  # 3
qacalc.multiply(4, 3)  # 12
qacalc.divide(10, 4)   # 2.5
```

`divide` raises `ZeroDivisionError` if the second argument is `0`:

```python
qacalc.divide(1, 0)
# ZeroDivisionError: division by zero: b must not be 0
```

## Command-line interface

The `qacalc` command supports the `add` and `subtract` subcommands:

```bash
$ qacalc add 2 3
5
$ qacalc subtract 5 2
3
```

It can also be run as a module, without installing the console script:

```bash
$ python -m qacalc add 2 3
5
```

`multiply` and `divide` are only available through the Python API; they are
not currently exposed as CLI subcommands.
