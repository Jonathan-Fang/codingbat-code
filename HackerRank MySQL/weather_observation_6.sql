-- select distinct(CITY) from STATION where "a","e","i","o","u" in CITY
select distinct(CITY) from STATION where CITY like 'a%' or CITY like 'e%' or CITY like 'i%' or CITY like 'o%' or CITY like 'u%'
-- solved with eddy's help
