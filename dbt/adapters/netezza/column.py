from dataclasses import dataclass

from dbt.adapters.base.column import Column


@dataclass
class NetezzaColumn(Column):
    TYPE_LABELS = {
        "STRING": "VARCHAR(4000)",
        "TIMESTAMP": "TIMESTAMP",
        "FLOAT": "DOUBLE",
        "INTEGER": "INT",
        "BOOLEAN": "BOOLEAN",
        "RECORD": "RECORD",
    }

    @classmethod
    def string_type(cls, size: int) -> str:
        return "character varying({})".format(size)