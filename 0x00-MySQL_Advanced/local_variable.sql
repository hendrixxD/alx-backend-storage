-- using local variable
DELIMETER $$
CREATE PROCEDURE local_variable()
BEGIN		-- declare local variable
DECLARE a INT DEFAULT 10;
DECLARE b. c INT; -- using local variables
SET a = a+ 10;
SET b = 2;
SET c = a + b;
-- a sub block
	BEGIN
	DECLARE c INT;
	SET c = 5;
	/* local variable c takes precedence over the one of the
same name declared in the enclosing block. */
	SELECT a, b, c;
	END;
SELECT a, b, c;
END$$
