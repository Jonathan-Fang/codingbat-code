-- Prompt: Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-11/problem?isFullScreen=true
-- Status: Solved October 5, 2023

select DISTINCT CITY 
from STATION 
where (CITY not like 'a%'
and CITY not like 'e%' 
and CITY not like 'i%' 
and CITY not like 'o%' 
and CITY not like 'u%')
or (CITY not like '%a'
and CITY not like '%e'
and CITY not like '%i'
and CITY not like '%o'
and CITY not like '%u');

-- X a%a
-- X b%a
-- X a&b
-- V b&b

-- Status, unsolved; Skills, SQL (Basic) and SQL(Intermediate)
