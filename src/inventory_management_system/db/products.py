import sqlite3


def add_product(
    conn, SKU, name, category, supplier_id, unit_price, quantity, reorder_level
):
    """Adds a product to our db

    Args:
        conn (sqlite connection): connection to the db
        SKU (str): unique number for each product
        name (str): name of product
        category (str): category of product
        supplier_id (int): id of the supplier
        unit_price (int): price in cents
        quantity (int): number of products
        reorder_level (int): threshold to reorder products at

    Returns:
        _type_: _description_
    """
    with conn:
        cursor = conn.execute(
            "INSERT INTO products(SKU, name, category, supplier, unit_price, quantity, reorder_level) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (SKU, name, category, supplier_id, unit_price, quantity, reorder_level),
        )
    return cursor.lastrowid
