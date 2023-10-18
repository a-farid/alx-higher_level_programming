-- List all records of a table
-- Query to list all records of the table second_table who have name value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
