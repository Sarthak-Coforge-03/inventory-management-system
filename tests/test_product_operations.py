import pytest

from inventory_management_system.db.products import (
    add_product,
    change_product_price,
    delete_product,
    get_product_with_supplier,
)


@pytest.fixture
def product(mem_db, supplier_id):
    return add_product(mem_db, "A-01", "Chair", "furniture", supplier_id, 1000, 10, 10)


def test_add_product(mem_db, supplier_id):
    """test for the add product function

    Args:
        mem_db (_type_): connection to memory db fixture
        supplier_id (_type_): fixture for adding a supplier
    """
    row = add_product(mem_db, "A-01", "Chair", "furniture", supplier_id, 1000, 10, 10)
    assert row["product_id"] == 1
    assert row["name"] == "Chair"
    assert row["SKU"] == "A-01"


def test_change_product_price(mem_db, product):
    """Test for change product price

    Args:
        mem_db (_type_): connection to memory db fixture
        product (_type_): fixture to add supplier and connected product
    """
    target_sku = product["SKU"]
    current_price = mem_db.execute(
        "SELECT unit_price FROM products WHERE SKU = ?", (target_sku,)
    ).fetchone()["unit_price"]
    new_sku = change_product_price(mem_db, target_sku, current_price + 1000)["SKU"]
    new_price = mem_db.execute(
        "SELECT unit_price FROM products WHERE SKU = ?", (new_sku,)
    ).fetchone()["unit_price"]
    assert new_sku == target_sku
    assert new_price > current_price


def test_get_product_with_supplier_name(mem_db, product):
    """test to get product joined to supplier name

    Args:
        mem_db (_type_): connection to memory db fixture
        product (_type_): fixture to add supplier and connected product
    """
    sku = product["SKU"]
    row = get_product_with_supplier(mem_db, sku)
    supplier_id = mem_db.execute(
        "SELECT id FROM suppliers WHERE id = ?", (row["supplier"],)
    ).fetchone()["id"]
    assert row["supplier"] == supplier_id


def test_delete_product(mem_db, product):
    """test to see if delete product works

    Args:
        mem_db (_type_): connection to memory db fixture
        product (_type_): fixture to add supplier and connected product
    """
    before = mem_db.execute("SELECT COUNT(*) AS n FROM products").fetchone()["n"]
    deleted = delete_product(mem_db, product["SKU"])
    after = mem_db.execute("SELECT COUNT(*) AS n FROM products").fetchone()["n"]
    assert deleted["SKU"] == product["SKU"]
    assert after == before - 1
