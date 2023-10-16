-- Prompt: Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.
-- Link: https://www.hackerrank.com/challenges/name-of-employees/problem?isFullScreen=true
-- Status: Solved before October 16, 2023

select name from Employee order by name ASC;