

-- 문제 1

SELECT productCode, productName, MSRP FROM products
WHERE MSRP > (
	SELECT AVG(MSRP) 
    FROM products
)
ORDER BY MSRP;

-- 문제 2

SELECT customerNumber, customerName FROM customers
WHERE customerNumber IN (
	SELECT customerNumber
    FROM orders 
    WHERE orderDate BETWEEN '2003-01-06' AND '2003-03-26'
)
ORDER BY customerNumber;


-- 문제 3

SELECT productCode, productName, productLine, MSRP FROM products
WHERE MSRP IN (
	SELECT MAX(MSRP)
    FROM products
    WHERE productLine = 'Classic Cars'
);


-- 문제 4

SELECT customerNumber, customerName, country FROM customers
WHERE country IN (
	SELECT MAX(country)
    FROM customers
)
ORDER BY customerNumber;


-- 문제 5

SELECT customerNumber, customerName, orderNumber
FROM (
	SELECT t1.customerNumber, customerName, orderNumber
    FROM orders AS t1
    INNER JOIN customers AS t2
		ON t1.customerNumber = t2.customerNumber
	) AS findName
WHERE
	orderNumber = (SELECT max(orderNumber) FROM orders);
    

-- 문제 5 해답

SELECT customers.customerNumber, customerName, COUNT(orders.customerNumber) as order_count
FROM customers
JOIN orders ON customers.customerNumber = orders.customerNumber
GROUP BY orders.customerNumber
ORDER BY order_count DESC
LIMIT 1;


-- 문제 6

SELECT productCode, productName 
FROM (
	SELECT t1.orderDate, t2.orderNumber, t3.productCode, t3.productName
    FROM orders AS t1
    INNER JOIN orderdetails AS t2
		ON t1.orderNumber = t2.orderNumber
	INNER JOIN products AS t3
		ON t2.productCode = t3.productCode
	) AS findName
WHERE
	orderDate = orderDate BETWEEN '2004-01-01' AND '2004-12-31'
    ORDER BY productCode DESC;
    
-- 문제 6  해답
SELECT DISTINCT p.productCode, p.productName
FROM orders o
INNER JOIN orderdetails od USING (orderNumber)
INNER JOIN products p USING (productCode)
WHERE o.orderDate BETWEEN '2004-01-01' AND '2004-12-31'
ORDER BY p.productCode DESC;