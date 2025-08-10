SELECT email as EMAIL
FROM Person
GROUP BY email
HAVING COUNT(Person.email)>1