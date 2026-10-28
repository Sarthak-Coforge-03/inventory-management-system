CREATE TABLE suppliers (

) STRICT;

CREATE TABLE products (
    SKU TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    supplier TEXT NOT NULL,
    unit_price DECIMAL NOT NULL,
    quantity INT NOT NULL,
    reorder_level INT NOT NULL
) STRICT;

CREATE TABLE sales (

) STRICT;

CREATE TABLE sale_items (
    product TEXT NOT NULL REFERENCES products(SKU),
    quantity INT NOT NULL,
    price DECIMAL NOT NULL
) STRICT;

CREATE TABLE stock_movements (

) STRICT;