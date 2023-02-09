-- creates a process
CREATE PROCEDURE lists_names()
SELECT * FROM new_names;##

-- the above is same as:
CREATE PROCEDURE list_names()
COMMENT ''
LANGUAGE SQL
NOT DETERMINISTIC
CONTAINS SQL
SQL QUERY DEFINER
SELECT * FROM new_names;
$$
