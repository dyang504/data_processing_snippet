/* 1. Create table */
CREATE TABLE ticket2019 (
	COLUMNS [DATA TYPE],
	...
);

/* 2. Import data from csv file */
Copy [Target Table Name]
FROM 'Path/to/file'
WITH csv
HEADER
ENCODING 'GBK';

/* 3. Save file to dask */
COPY (
	[QUERIES]
	/* When join tables the order of clauses after ON affect the type of JOIN(LEFT JOIN, RIGHT JOIN, etc). */
)
TO 
'D:/Result.csv'
WITH CSV DELIMITER ',' HEADER;