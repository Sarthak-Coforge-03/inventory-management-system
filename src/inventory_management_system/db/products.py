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
        sqlite row: product_id, name, and SKU of the added product
    """
    with conn:
        cursor = conn.execute(
            "INSERT INTO products(SKU, name, category, supplier, unit_price, quantity, reorder_level) "
            "VALUES (?, ?, ?, ?, ?, ?, ?) "
            "RETURNING id AS product_id, name, SKU",
            (SKU, name, category, supplier_id, unit_price, quantity, reorder_level),
        )
        return cursor.fetchone()


def get_product_with_supplier(conn, SKU):
    """Get the product with supplier name based on sku

    Args:
        conn (_type_): sqlite connection
        SKU (str): unique product identifier

    Returns:
        sqlite row : row that has been retrieved with supplier name column added
    """
    with conn:
        cursor = conn.execute(
            "SELECT p.*, s.name AS supplier_name "
            "FROM products p "
            "INNER JOIN suppliers s "
            "ON p.supplier = s.id "
            "WHERE p.SKU = ?",
            (SKU,),
        )
    return cursor.fetchone()


def change_product_price(conn, SKU, unit_price):
    """change the product of given

    Args:
        conn (_type_): connection to the db
        SKU (_type_): unique number for each product
        unit_price (_type_): new price in cents

    Returns:
        sqlite row: product name, sku, new price
    """

    with conn:
        cursor = conn.execute(
            "UPDATE products "
            "SET unit_price = ? "
            "WHERE SKU = ? "
            "RETURNING SKU, name, unit_price",
            (unit_price, SKU),
        )
        return cursor.fetchone()


def delete_product(conn, SKU):
    """delete the product with given sku

    Args:
        conn (connection): sqlite 3 connection
        SKU (str): unique string identifier

    Returns:
        sqlite row: sku and name of deleted product
    """
    with conn:
        cursor = conn.execute(
            "DELETE FROM products WHERE SKU = ? RETURNING SKU, name", (SKU,)
        )
        return cursor.fetchone()
