-- Total sales & profit
SELECT SUM(Sales), SUM(Profit) FROM orders;

-- Sales by Region
SELECT Region, SUM(Sales) 
FROM orders
GROUP BY Region
ORDER BY SUM(Sales) DESC;

-- Top 10 Products by Sales
SELECT [Product Name], SUM(Sales) as sales
FROM orders
GROUP BY [Product Name]
ORDER BY sales DESC
LIMIT 10;
