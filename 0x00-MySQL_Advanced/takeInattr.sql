-- using IN to take in values from users
DELIMITER ##
CREATE PROCEDURE proc_IN(IN var1 INT)
    BEGIN
    SELECT * FROM JOBS LIMIT var1;
    END##

-- Result: CALL proc_IN(2)##
-- +------+--------+------------+
-- | id   | userid | name       |
-- +------+--------+------------+
-- |    1 | 1      | joshua dan |
-- +------+--------+------------+

