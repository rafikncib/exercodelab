-- # write your SQL statement here: you are given a table 'removeexclamationmarks' with column 's', return a table with column 's' and your result in a column named 'res'.

select s,replace(s,'!','') as res
from removeexclamationmarks