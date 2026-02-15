# DuckDB SQLLogicTest

> Warning: experimental!

## Overview

This is a library for running SQLLogicTest tests on the DuckDB database engine. It leverages DuckDB's Python distribution to easily run tests against various versions of DuckDB. This is especially useful when developing and maintaining DuckDB extensions.

## Usage

The SQLLogicTest runner can be used through pytest, for example:
```bash
python3 -m pytest sqllogic/test_sqllogic.py --duckdb-root-dir $HOME/duckdb --path test/sql/types/list/list_distinct.test
```

## Installation

The package is not on PyPI, so you must install it directly from GitHub. Make sure you are in your project's virtual environment.

### Standard Install

For most use cases, you can install the package directly using pip:
```bash
pip install git+https://github.com/duckdb/duckdb-sqllogictest-python
```
