-- Prompt: Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name).
-- If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true
-- Status: not solved yet

select min(city), min(length(city)) from station ORDER BY city ASC;
select max(city), max(length(city)) from station ORDER BY city ASC;
