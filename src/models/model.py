import sqlite3
from config import DB_PATH
from typing import Any, List, Literal, Optional, Union, Dict
from .sql import INVOICE, PRIZE, PRIZE_TYPES, PRIZE_TYPES_VALUES, PRIZE_TYPES_INDEX


def connect_db() -> sqlite3.Connection:
    """The connect_db function connects to the database."""

    return sqlite3.connect(
        DB_PATH, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
    )


def query(
    script: str,
    params: Optional[Union[List[tuple], Dict[str, Any], None]] = None,
    mode: Optional[Union[Literal["script", "many"], None]] = None,
) -> Union[List, None]:
    """The query function query the database based on `script`, `params` and `mode`."""

    invoiceCli = connect_db()

    with invoiceCli:
        if mode == "script":
            return invoiceCli.executescript(script).fetchall()
        elif mode == "many":
            if params is None:
                raise TypeError("parames must be specified")
            return invoiceCli.executemany(script, params).fetchall()

        if params is not None:
            return invoiceCli.execute(script, params).fetchall()

        return invoiceCli.execute(script).fetchall()


def init_db() -> None:
    """The init_db function initializes the database."""

    sql_script = f"""
    BEGIN TRANSACTION;
    {INVOICE}
    {PRIZE}
    {PRIZE_TYPES}
    {PRIZE_TYPES_VALUES}
    {PRIZE_TYPES_INDEX}
    COMMIT;
    """
    query(sql_script, mode="script")
