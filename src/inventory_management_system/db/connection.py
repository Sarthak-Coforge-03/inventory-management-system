import sqlite3
from pathlib import Path

data_dir = Path(__file__).parents[3] / "data"
data_dir.mkdir(parents=True, exist_ok=True)


def connect(db_name="inventory.db") -> sqlite3.Connection:
    """Returns a sqlite 3 connection
    sets row factory to sqlite3.Row
    Keeps pragma on
    Args:
        db_name (str, optional): the db to connect to. Defaults to "inventory.db". Allows to also pass in :memory:

    Returns:
        sqlite3.Connection: sqlite 3 connection
    """
    if db_name == ":memory:":
        connection = sqlite3.connect(db_name)
    else:
        connection = sqlite3.connect(data_dir / db_name)
    connection.execute("PRAGMA foreign_keys = ON")
    connection.row_factory = sqlite3.Row
    return connection
