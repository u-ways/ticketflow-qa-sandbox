# qacalc

A minimal calculator package with a Python API and a CLI.

## Installation

Install from a local clone:

```console
pip install .
```

For development (editable install):

```console
pip install -e .
```

To also install test dependencies:

```console
pip install -e '.[test]'
```

## Python API usage

```python
import qacalc

qacalc.add(2, 3)
# 5
```

```python
import qacalc

qacalc.subtract(10, 4)
# 6
```

```python
import qacalc

qacalc.multiply(6, 7)
# 42
```

```python
import qacalc

qacalc.divide(7, 2)
# 3.5
```

Dividing by zero raises `ZeroDivisionError` with a descriptive message:

```python
import qacalc

qacalc.divide(5, 0)
# ZeroDivisionError: division by zero: cannot divide 5 by 0
```

## CLI usage

Available as the installed console script (`qacalc <op> A B`) or as a module
(`python -m qacalc <op> A B`) — both forms are equivalent.

```console
$ qacalc add 2 3
5
```

```console
$ qacalc subtract 10 4
6
```

```console
$ qacalc multiply 6 7
42
```

```console
$ qacalc divide 7 2
3.5
```

Dividing by zero prints an error to stderr and exits with status 1:

```console
$ qacalc divide 5 0
error: division by zero: cannot divide 5 by 0
```

## Running tests

```console
pip install -e '.[test]'
pytest -q
```
