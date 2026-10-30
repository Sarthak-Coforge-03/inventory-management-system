from pathlib import Path

import pytest

from inventory_management_system import connect

SCHEMA_PATH = Path(__file__).with_name("schema.sql")


@pytest.fixture
def mem_db():
    """Pytest fixture to return a sqlite connection to a memory db with tables.

    Returns:
        sqlite connection: in-memory db
    """
    conn = connect(":memory:")
    conn.executescript(SCHEMA_PATH.read_text())
    return conn
