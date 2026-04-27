use northwind;

-- 2) Write a query to identify the products where the unit price is $7.50 or less

select distinct productID, ProductName, UnitPrice
from products 
where UnitPrice <= 7.50;

-- 3) What are the products that we carry where we have no units on hand, but 1 or more
-- units are on backorder? Write a query that answers this question.

select ProductID, ProductName, UnitsInStock, UnitsOnOrder
from products 
where UnitsInStock = 0 
and UnitsOnOrder >= 1

-- 4). Examine the products table. How does it identify the type (category) of each item
-- sold? Where can you find a list of all categories? Write a set of queries to answer these
-- questions, ending with a query that creates a list of all the seafood items we carry

select *
from products 

SELECT distinct CategoryID
from products 

SELECT *
from categories 

SELECT DISTINCT CategoryName, CategoryID
FROM categories

SELECT * 
FROM products
where CategoryID = '8'
-- 12 rows 

-- 5. Examine the products table again. How do you know what supplier each product
-- comes from? Where can you find info on suppliers? Write a set of queries to find the
-- specific identifier for "Tokyo Traders" and then find all products from that supplier

SELECT * 
FROM products

select * 
from suppliers 
where CompanyName like '%Tokyo Traders%'
-- 4 

SELECT * 
FROM products
where SupplierID = '4'
-- 3 

-- 6. How many employees work at northwind? What employees have "manager"
-- somewhere in their job title? Write queries to answer each question

select * 
from employees
-- 9 

select * 
from employees
where Title like '%anager%'
-- 1 

