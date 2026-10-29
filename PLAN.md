# 5 TABLE SETUP
1. Suppliers can have many products but a product can only have 1 supplier.
2. One sale can have many sales items while each sale item can have one sale and one product.
3. One product can have many stock movements. Each movement belongs to one product

## Suppliers
1. Table to manage supplier identity
## Products
1. What the store sells and quantity of it
## Sales
1. A record of checkout events
## Sale Items
1. The product, how many, and price charged. 
## Stock Movemements
1. Stock movements are the audit logs, keeping what changed