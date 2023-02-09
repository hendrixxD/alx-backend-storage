-- using user defined variables
DELIMETER ##
CREATE PROCEDURE user_variable()
BEGIN
	SET @x = 15;
	SET @y = 10;
	SELECT @x, @y, @x-@y;
END##
