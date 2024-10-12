from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="duckdb_sqllogictest",
    version="0.0.1",
    author="Thijs Bruineman",
    author_email="thijs@duckdblabs.com",
    description="A Python package for running SQLLogicTest tests with DuckDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/duckdb/duckdb-sqllogictest-python",
    packages=find_packages(),
    install_requires=[
        "duckdb",
        "termcolor"
    ],
    extras_require={
    },
    entry_points={
        "console_scripts": [
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
)