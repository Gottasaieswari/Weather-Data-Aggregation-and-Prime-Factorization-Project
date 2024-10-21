-- Increase the price of all products by 10%
UPDATE products
SET price = price * 1.10;

-- Display the new prices with product names
SELECT name, price
FROM products;
