CREATE TABLE IF NOT EXISTS suppliers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
) STRICT;

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    SKU TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    supplier INTEGER NOT NULL REFERENCES suppliers(id),
    unit_price INTEGER NOT NULL CHECK (unit_price >= 0),
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    reorder_level INTEGER NOT NULL CHECK (reorder_level >= 0)
) STRICT;

CREATE INDEX IF NOT EXISTS idx_products_supplier ON products(supplier);

CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    sold_at TEXT NOT NULL
) STRICT;

CREATE TABLE IF NOT EXISTS sale_items (
    id INTEGER PRIMARY KEY,
    product INTEGER NOT NULL REFERENCES products(id),
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    price INTEGER NOT NULL CHECK (price >= 0),
    sale_id INTEGER NOT NULL REFERENCES sales(id),
    UNIQUE (sale_id, product)
) STRICT;

CREATE TABLE IF NOT EXISTS stock_movements (
    movement_id INTEGER PRIMARY KEY,
    product INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    change INTEGER NOT NULL,
    reason TEXT NOT NULL CHECK (reason IN ('restock', 'adjustment', 'sale')),
    moved_at TEXT NOT NULL
) STRICT;