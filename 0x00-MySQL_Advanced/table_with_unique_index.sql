-- a table with a PK of ID
-- and a unique index of ( ID )

CREATE TABLE imd_table (
	Lname VARCHAR(200),
	Fname VARCHAR(200),
	PRIMARY KEY ( ID ),
	UNIQUE INDEX ( ID )
);
