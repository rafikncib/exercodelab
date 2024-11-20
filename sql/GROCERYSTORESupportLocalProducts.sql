-- Replace with your SQL Query
 
SELECT count(products) as products , country
FROM products
where  country IN('United States of America', 'Canada') 
GROUP BY country
ORDER BY products DESC
;

