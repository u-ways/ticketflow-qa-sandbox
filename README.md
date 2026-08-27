# qacalc

A simple calculator package.

## Installation

`qacalc` is not published to PyPI. Install it from source (editable install):

```bash
pip install -e .
```

To also install test dependencies (`pytest`):

```bash
pip install -e ".[test]"
```

Requires Python >= 3.9.

## Python API

The `qacalc` package exposes four functions: `add`, `subtract`, `multiply`, and `divide`.

### add

```python
>>> from qacalc import add
>>> add(2, 3)
5
```

### subtract

```python
>>> from qacalc import subtract
>>> subtract(5, 3)
2
```

### multiply

```python
>>> from qacalc import multiply
>>> multiply(4, 6)
24
```

### divide

```python
>>> from qacalc import divide
>>> divide(6, 3)
2.0
```

Dividing by zero raises a `ZeroDivisionError` with a specific message (rather than Python's default error):

```python
>>> from qacalc import divide
>>> divide(5, 0)
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero: b must not be 0
```

## CLI

Installing the package registers a `qacalc` console script (`qacalc = "qacalc.cli:main"`). It can also be invoked as `python -m qacalc`. Only the `add` and `subtract` operations are available via the CLI:

```
$ qacalc --help
usage: qacalc [-h] {add,subtract} ...

A simple calculator.

positional arguments:
  {add,subtract}

options:
  -h, --help      show this help message and exit
```

Examples:

```
$ qacalc add 2 3
5

$ qacalc subtract 5 3
2

$ qacalc subtract 2 5
-3

$ python -m qacalc add 10 15
25
```

Note: `multiply` and `divide` are not exposed as CLI subcommands, only as Python functions.
