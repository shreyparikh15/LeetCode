SELECT e2.name as Employee
FROM Employee e1
LEFT JOIN Employee e2
ON e1.id = e2.managerId
WHERE e1.salary < e2.salary