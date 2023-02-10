-- Write a SQL script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans

-- Import this table dump: metal_bands.sql.zip
-- Column names must be: origin and nb_fans
-- Your script can be executed on any database

SELECT origin, fans nb_fans
FROM metal_bands
ORDER BY nb_fans
