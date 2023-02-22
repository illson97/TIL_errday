

-- 문제 1

SELECT employeeNumber, lastName, firstName, city FROM employees
INNER JOIN offices ON employees.officeCode = offices.officeCode
ORDER BY employeeNumber;

-- 문제 2

SELECT customerNumber, officeCode, customers.city, offices.city FROM customers
LEFT JOIN offices ON offices.city = customers.city
ORDER BY customerNumber DESC;


-- 문제 3

SELECT customerNumber, officeCode, customers.city, offices.city FROM customers
RIGHT JOIN offices ON offices.city = customers.city
ORDER BY customerNumber DESC;

-- 문제 4

SELECT customerNumber, officeCode, customers.city, offices.city FROM customers
INNER JOIN offices ON offices.city = customers.city
ORDER BY customerNumber DESC;

-- 문제 5

문제 2 번은 customer 테이블에 offices 테이블이 속하는 부분을 조인 시킨 것이고
문제 3 번은 offices 테이블에 customer 테이블이 속하는 부분을 조인 시킨 것이고
문제 4 번은 두 테이블의 교집합만 표시를 하는 것이기 때문에 순서와 내용 접합 차이로 인해 결과가 차이난다.;


-- 문제 6

SELECT customerNumber, officeCode, customers.city, offices.city FROM customers
LEFT JOIN offices ON offices.city = customers.city
UNION
SELECT customerNumber, officeCode, customers.city, offices.city FROM customers
RIGHT JOIN offices ON offices.city = customers.city
ORDER BY customerNumber DESC;


-- 문제 7

SELECT orderdetails.orderNumber, orderdate FROM orderdetails
INNER JOIN orders ON orderdetails.orderNumber = orders.orderNumber
ORDER BY orderdetails.orderNumber;

-- 문제 8

SELECT orderdetails.ordernumber, orderdetails.productCode, products.productName
FROM orderdetails INNER JOIN products ON orderdetails.productCode = products.productCode
ORDER BY orderNumber;

-- 문제 9

SELECT orderdetails.orderNumber, orderdetails.productCode, orders.orderDate, products.productName 
FROM orderdetails INNER JOIN orders ON orderdetails.orderNumber = orders.orderNumber
INNER JOIN products ON orderdetails.productCode = products.productCode
ORDER BY orderNumber;