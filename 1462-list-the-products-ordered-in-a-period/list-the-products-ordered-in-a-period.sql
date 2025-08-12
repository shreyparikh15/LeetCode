SELECT p.product_name, SUM(o.unit) as unit 
FROM Products p
LEFT JOIN Orders o
ON p.product_id = o.product_id
WHERE MONTH(o.order_date)=2 AND YEAR(o.order_date)=2020
GROUP BY o.product_id
HAVING SUM(o.unit)>=100