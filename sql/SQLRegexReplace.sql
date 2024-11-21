/*  SQL  */
SELECT 
    project, 
    commits, 
    contributors, 
    REPLACE(
        REPLACE(
            REPLACE(
                REPLACE(
                    REPLACE(
                        REPLACE(
                            REPLACE(
                                REPLACE(
                                    REPLACE(
                                        REPLACE(address, '0', '!'), '1', '!'), '2', '!'), '3', '!'), '4', '!'), '5', '!'), '6', '!'), '7', '!'), '8', '!'), '9', '!') AS address
FROM 
    repositories;
