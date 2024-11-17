-- # write your SQL statement here: you are given a table 'ispalindrome' with column 'str', return a table with column 'str' and your result in a column named 'res'.

select str, reverse(lower(str))=lower(str) as res
from ispalindrome