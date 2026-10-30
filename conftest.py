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


@pytest.fixture
def supplier_id(mem_db):
    """Insert one supplier and return its id."""
    with mem_db:
        cursor = mem_db.execute(
            "INSERT INTO suppliers(name) VALUES (?)",
            ("abc",),
        )
    return cursor.lastrowid
