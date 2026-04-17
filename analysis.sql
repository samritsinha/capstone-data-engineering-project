USE ecommerce;

SELECT customer_id, SUM(quantity) AS total_orders
FROM orders
GROUP BY customer_id;

SELECT product_id, SUM(quantity) AS total_sold
FROM orders
GROUP BY product_id
ORDER BY total_sold DESC;

SELECT order_date, COUNT(*) AS total_orders
FROM orders
GROUP BY order_date;