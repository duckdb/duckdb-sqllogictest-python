# DuckDB SQLLogicTest

> Warning: experimental!

## Overview

This is a library for running SQLLogicTest tests on the DuckDB database engine. It leverages DuckDB's Python distribution to easily run tests against various versions of DuckDB. This is especially useful when developing and maintaining DuckDB extensions.

## Usage

The SQLLogicTest runner can be used through pytest, for example:
```bash
python3 -m pytest sqllogic/test_sqllogic.py --duckdb-root-dir $HOME/duckdb --path test/sql/types/list/list_distinct.test
```
