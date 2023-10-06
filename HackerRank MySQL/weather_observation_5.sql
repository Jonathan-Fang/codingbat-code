-- https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true

select min(city), min(length(city)) from station ORDER BY city ASC;
select max(city), max(length(city)) from station ORDER BY city ASC;
-- not solved yet