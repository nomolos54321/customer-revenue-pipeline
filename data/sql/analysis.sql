-- 1. Total Revenue
SELECT SUM(Revenue) AS total_revenue
FROM retail_transactions;

-- 2. Revenue by Country
SELECT Country, SUM(Revenue) AS revenue
FROM retail_transactions
GROUP BY Country
ORDER BY revenue DESC;

-- 3. Top 10 Products by Revenue
SELECT Description, SUM(Revenue) AS revenue
FROM retail_transactions
GROUP BY Description
ORDER BY revenue DESC
LIMIT 10;

-- 4. Monthly Revenue Trend
SELECT YearMonth, SUM(Revenue) AS revenue
FROM retail_transactions
GROUP BY YearMonth
ORDER BY YearMonth;

-- 5. Top Customers by Spend
SELECT `Customer ID`, SUM(Revenue) AS total_spent
FROM retail_transactions
GROUP BY `Customer ID`
ORDER BY total_spent DESC
LIMIT 10;
