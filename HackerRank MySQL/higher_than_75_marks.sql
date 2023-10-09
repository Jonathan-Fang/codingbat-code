-- Prompt: Query the Name of any student in STUDENTS who scored higher than  Marks. 
-- Order your output by the last three characters of each name. 
-- If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
-- Link: https://www.hackerrank.com/challenges/more-than-75-marks/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
-- Status:

select NAME, RIGHT(NAME, 3) AS EXTRACTEDSTR FROM STUDENTS where Marks > 75 and ('%%%' like '%%%') ORDER BY ID ASC;

select NAME 
from STUDENTS 
where Marks > 75 
ORDER BY ID ASC;

-- where NAME like '%