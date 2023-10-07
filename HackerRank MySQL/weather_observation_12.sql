-- Prompt: Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-12/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
-- Status: Solved October 6, 2023

-- Use-Cases
-- X aa&bb
-- X aa&aa
-- X bb&aa
-- X bb&bb

select DISTINCT CITY
from STATION
where (CITY not like 'a%'
and CITY not like 'e%' 
and CITY not like 'i%' 
and CITY not like 'o%' 
and CITY not like 'u%')
and (CITY not like '%a'
and CITY not like '%e'
and CITY not like '%i'
and CITY not like '%o'
and CITY not like '%u');