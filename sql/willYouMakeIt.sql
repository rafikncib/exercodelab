--# write your SQL statement here: you are given a table 'zerofuel' with columns 'distance_to_pump', 'mpg' and 'fuel_left', return a table with all the columns and your result in a column named 'res'.

select distance_to_pump, mpg, fuel_left, (distance_to_pump <=(mpg*fuel_left)) as res
from zerofuel