from contextlib import closing
from pathlib import Path

from inventory_management_system import connect

SCHEMA_PATH = Path(__file__).with_name("schema.sql")

suppliers_seed = [
    ("Acme Hardware",),
    ("Summit Fasteners",),
    ("ColorLot Paint",),
    ("Lakeside Lumber",),
]
products_seed = [
    ("HAM-001", "Claw hammer", "tools", 1, 1299, 15, 5),
    ("SCR-010", "Screwdriver set", "tools", 1, 899, 20, 8),
    ("WRE-A12", "Adjustable wrench", "tools", 1, 1599, 7, 4),
    ("TAP-025", "Measuring tape", "tools", 1, 699, 18, 8),
    ("NAI-100", "Framing nails", "fasteners", 2, 599, 50, 20),
    ("SCW-020", "Wood screws", "fasteners", 2, 399, 8, 10),
    ("ANC-050", "Wall anchors", "fasteners", 2, 299, 2, 10),
    ("PNT-WHT", "Interior white paint", "paint", 3, 1999, 12, 6),
    ("PNT-BLU", "Interior blue paint", "paint", 3, 1999, 10, 6),
    ("BRS-200", "2 inch brush", "paint", 3, 499, 25, 10),
    ("PLY-4X8", "Plywood 4x8", "lumber", 4, 2499, 3, 5),
    ("STU-2X4", "2x4 stud", "lumber", 4, 499, 40, 15),
]
sales_seed = [
    ("2026-09-01T10:00:00",),
    ("2026-09-08T14:30:00",),
    ("2026-09-15T09:15:00",),
    ("2026-09-22T16:45:00",),
    ("2026-09-29T11:20:00",),
]
sale_items_seed = [
    (1, 1, 1299, 1),
    (2, 1, 899, 1),
    (5, 2, 599, 1),
    (6, 1, 399, 2),
    (11, 1, 2499, 2),
    (8, 1, 1999, 3),
    (9, 1, 1999, 3),
    (10, 2, 499, 3),
    (3, 1, 1599, 4),
    (12, 4, 499, 4),
    (1, 1, 1299, 5),
    (8, 1, 1999, 5),
]
stock_movements_seed = []

suppliers_query = "INSERT INTO suppliers(name) VALUES (?)"
products_query = "INSERT INTO products(SKU, name, category, supplier, unit_price, quantity, reorder_level) VALUES (?, ?, ?, ?, ?, ?, ?)"
sales_query = "INSERT INTO sales(sold_at) VALUES (?)"
sale_items_query = (
    "INSERT INTO sale_items(product, quantity, price, sale_id) VALUES (?, ?, ?, ?)"
)
stock_movements_query = (
    "INSERT INTO stock_movements(product, change, reason, moved_at) VALUES (?, ?, ?, ?)"
)

if __name__ == "__main__":
    with closing(connect()) as conn:
        conn.executescript(SCHEMA_PATH.read_text())
        with conn:
            conn.executemany(suppliers_query, suppliers_seed)
            conn.executemany(products_query, products_seed)
            conn.executemany(sales_query, sales_seed)
            conn.executemany(sale_items_query, sale_items_seed)
            conn.executemany(stock_movements_query, stock_movements_seed)
        print("Created and seeded folowing counts:")
        print(
            "suppliers:",
            conn.execute("SELECT COUNT(*) AS n FROM suppliers").fetchone()["n"],
        )
        print(
            "products:",
            conn.execute("SELECT COUNT(*) AS n FROM products").fetchone()["n"],
        )
        print("sales:", conn.execute("SELECT COUNT(*) AS n FROM sales").fetchone()["n"])
        print(
            "sale_items:",
            conn.execute("SELECT COUNT(*) AS n FROM sale_items").fetchone()["n"],
        )
        print(
            "stock_movements:",
            conn.execute("SELECT COUNT(*) AS n FROM stock_movements").fetchone()["n"],
        )
