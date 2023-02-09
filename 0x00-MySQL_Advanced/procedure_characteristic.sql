-- The COMMENT characteristic is a MySQL extension. It is used to describe the stored routine and the information is displayed by the SHOW CREATE PROCEDURE statements.
COMMENT 'string'
-- The LANGUAGE characteristic indicates that the body of the procedure is written in SQL.
| LANGUAGE SQL
-- NOT DETERMINISTIC, is informational, a routine is considered "deterministic"  if it always produces the same result for the same input parameters, and "not deterministic" otherwise.
| [NOT] DETERMINISTIC
-- CONTAINS SQL means there are no statements that read or write data, in the routine. For example statements SET @x = 1 or DO RELEASE_LOCK('abc'), which execute but neither read nor write data. This is the default if none of these characteristics is given explicitly.
-- NO SQL means routine contains no SQL statements.
-- READS SQL DATA means the routine contains statements that read data (for example, SELECT), but not statements that write data.
-- MODIFIES SQL DATA means routine contains statements that may write data (for example, INSERT or DELETE).
| { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
-- SQL SECURITY, can be defined as either SQL SECURITY DEFINER or SQL SECURITY INVOKER to specify the security context; that is, whether the routine executes using the privileges of the account named in the routine DEFINER clause or the user who invokes it.
-- This account must have permission to access the database with which the routine is associated. The default value is DEFINER. The user who invokes the routine must have the EXECUTE privilege for it, as must the DEFINER account if the routine executes in definer security context. 
| SQL SECURITY { DEFINER | INVOKER }
