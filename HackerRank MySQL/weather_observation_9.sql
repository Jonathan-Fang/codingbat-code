-- Prompt: Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-9/problem?isFullScreen=true
-- Status: Solved October 5, 2023

select DISTINCT CITY 
from STATION 
where CITY not like 'a%'
and CITY not like 'e%' 
and CITY not like 'i%' 
and CITY not like 'o%' 
and CITY not like 'u%';