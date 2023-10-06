-- Prompt: Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true
-- Status: Solved

select distinct CITY from STATION where CITY like '%a' or CITY like '%e' or CITY like '%i' or CITY like '%o' or CITY like '%u'