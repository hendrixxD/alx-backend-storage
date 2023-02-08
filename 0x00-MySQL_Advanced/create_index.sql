-- creating a table with an index

CREATE TABLE imd_table (ID int,
	Lname VARCHAR(200),
	Fname VARCHAR(200),
	DOB VARCHAR(255),
	INDEX ( ID ));
