use northwind;

-- 1. Write a query to list the product id, product name, and unit price of every product. This
-- time, display them in ascending order by price.

select distinct ProductID, ProductName, UnitPrice  
from products
order by UnitPrice ASC 

-- 2. What are the products that we carry where we have at least 100 units on hand? Order
-- them in descending order by price.

select *
from products
where UnitsInStock >= 100 
order by UnitPrice desc 

-- 3. What are the products that we carry where we have at least 100 units on hand? Order
-- them in descending order by price. If two or more have the same price, list those in
-- ascending order by product name.

select *
from products
where UnitsInStock >= 100 
order by UnitPrice desc, ProductName ASC

-- 4. Write a query against the orders table that displays the total number of distinct
-- customers who have placed orders, based on customer ID. Use an alias to label the
-- count calculation as CustomerCount.

select count(distinct CustomerID) as CustomerCount
from orders
-- 89 

-- 5. Write a query against the orders table that displays the total number of distinct
-- customers who have placed orders, by customer ID, for each country where orders
-- have been shipped. Again, use an alias to label the count as CustomerCount. Order
-- the list by the CustomerCount, largest to smallest.

select ShipCountry, count(distinct CustomerID)  as CustomerCount
from orders
group by ShipCountry 
order by CustomerCount desc

-- 6. What are the products that we carry where we have less than 25 units on hand, but 1
-- or more units of them are on order? Write a query that orders them by quantity on
-- order (high to low), then by product name.

select ProductName, UnitsInStock, UnitsOnOrder
from products 
where UnitsInStock <= 25 
and UnitsOnOrder >= 1 
and ProductName is not null
order by UnitsOnOrder desc, ProductName asc

-- 7. Write a query to list each of the job titles in employees, along with a count of how
-- many employees hold each job title.
select Title, count(EmployeeID)
from employees
group by Title

-- 8. What employees have a monthly salary that is between $2000 and $2500? Write a
-- query that orders them by job title
select EmployeeID, Title, Salary
from employees
where Salary between 2000 and 2500
order by Title asc

--1. Create a single query to list the product id, product name, unit price and category
name of all products. Order by category name and within that, by product name.
select ProductID, ProductName, UnitPrice, CategoryName
from products
join categories on products.CategoryID = categories.CategoryID
order by CategoryName, ProductName

--2. Create a single query to list the product id, product name, unit price and supplier
--name of all products that cost more than $75. Order by product name.
select ProductID, ProductName, UnitPrice, CompanyName
from products 
join suppliers on products.SupplierID = suppliers.SupplierID
where UnitPrice > 75
order by ProductName

--3. Create a single query to list the product id, product name, unit price, category name,
--and supplier name of every product. Order by product name.
select ProductID, ProductName, UnitPrice, CategoryName, CompanyName
from products 
join categories on products.CategoryID = categories.CategoryID
join suppliers on products.SupplierID = suppliers.SupplierID
order by ProductName

--4. Create a single query to list the order id, ship name, ship address, and shipping
--company name of every order that shipped to Germany. Assign the shipping company
--name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
--shipped to.

select OrderID, ShipName, ShipAddress, CompanyName as 'Shipper' 
from orders
join shippers on orders.ShipVia = shippers.ShipperID 
where ShipCountry like '%germany%'
order by Shipper, ShipName 

5. Start from the same query as above (#4), but omit OrderID and add logic to group by
ship name, with a count of how many orders were shipped for that ship name.
select ShipName, ShipAddress, CompanyName as Shipper, count(*) as OrdersShipped
from orders
join shippers on orders.ShipVia = shippers.ShipperID 
where ShipCountry like '%germany%'
group by ShipName, ShipAddress, CompanyName
order by Shipper

6. Create a single query to list the order id, order date, ship name, ship address of all
orders that included Sasquatch Ale.
∗ Hint: You will need to join on three tables to accomplish this. (One of these tables
has a sneaky space in the name, so you will need to surround it with backticks, like
this: `table name`)

select o.OrderID, OrderDate, ShipName, ShipAddress
from orders as o 
join `order details` as od on o.OrderID = od.OrderID
join products as p on od.ProductID = p.ProductID
where p.ProductName like '%asquatch al%'


7. Save your changes to 2A_using_joins.sql and use Git Bash to add, commit, and push
to DataAnalytics/week-03.