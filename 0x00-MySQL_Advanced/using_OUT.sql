-- using OUT
DELIMITER $$
CREATE PROCEDURE high_salary(OUT max_salary INT)
BEGIN
	SELECT MAX(max_salary) INTO max_salary FROM jobs;
END$$

-- calling procedure
CALL high_salary(@Max_salary)$$
SELECT max_salaty$$
