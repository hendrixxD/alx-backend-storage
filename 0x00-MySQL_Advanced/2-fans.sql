-- Write a SQL script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans

-- Import this table dump: metal_bands.sql.zip
-- Column names must be: origin and nb_fans
-- Your script can be executed on any database

WITH band_fans AS (
    SELECT origin, COUNT(*) as nb_fans
    FROM metal_bands
    GROUP BY origin
)
SELECT origin, nb_fans
FROM band_fans
ORDER BY nb_fans DESC;
