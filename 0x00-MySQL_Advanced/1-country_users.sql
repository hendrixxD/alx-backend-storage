-- Write a SQL script that creates a table users following these requirements:
-- 
-- With these attributes:
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
-- If the table already exists, your script should not fail
-- Your script can be executed on any database

-- DELIMITER ## ;
DELIMITER $$ ;
CREATE PROCEDURE table_users()
BEGIN
CREATE TABLE IF NOT EXISTS users (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
email CHAR(255) NOT NULL UNIQUE,
name CHAR(255),
COUNTRY ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US');
END$$
-- execute the below to resume the use of ;
-- DELIMITER;##
DELIMITER ; $$
