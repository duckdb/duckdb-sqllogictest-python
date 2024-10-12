from duckdb_sqllogictest.base_statement import BaseStatement
from duckdb_sqllogictest.token import Token


class Mode(BaseStatement):
    def __init__(self, header: Token, line: int, parameter: str):
        super().__init__(header, line)
        self.parameter = parameter
