# qacalc

A small calculator package providing basic arithmetic operations, available
both as a Python library and as a command-line tool.

## Installation

Install from a local checkout:

```sh
pip install .
```

For development, install with the `test` extra to also pull in `pytest`:

```sh
pip install -e ".[test]"
```

Requires Python >= 3.8.

## Python API usage

The package exposes four functions: `add`, `subtract`, `multiply`, and
`divide`.

```python
from qacalc import add, subtract, multiply, divide

add(2, 3)        # 5
add(2.5, 1.5)    # 4.0

subtract(5, 3)   # 2
subtract(2, 5)   # -3

multiply(4, 5)   # 20
multiply(2.5, 2) # 5.0

divide(10, 4)    # 2.5
divide(-6, -3)   # 2.0
```

Dividing by zero raises a `ZeroDivisionError` with a descriptive message:

```python
from qacalc import divide

try:
    divide(10, 0)
except ZeroDivisionError as e:
    print(e)  # cannot divide 10 by zero
```

## CLI usage

Installing the package also installs a `qacalc` console script. It supports
the `add` and `subtract` subcommands (each taking two positional numbers):

```sh
$ qacalc add 2 3
5

$ qacalc subtract 5 3
2

$ qacalc add -2 3
1
```

You can also run it as a module, without relying on the console script being
on your `PATH`:

```sh
$ python -m qacalc add 2.5 1.5
4.0
```

Note: `multiply` and `divide` are available in the Python API only; the CLI
currently supports just `add` and `subtract`.

## License

MIT — see [LICENSE](LICENSE).
