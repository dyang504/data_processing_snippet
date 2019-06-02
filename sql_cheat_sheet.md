## The Cheat Sheet of SQL And Deal with database
### Cheat Sheet
data 

**Key WORDS**

DISTINCT

`CASE` USAGE: 1. Add new category column;2. Exclude/clean unwanted values, a filter;3.`CASE` can use with other functions like `SUM`

**Basic Query Pattern**

	SELECT [DISTINCT] …, …
	FROM [table]
	WHERE <expr>
	GROUP BY [coloumns,…]
	HAVING <expr>
	ORDER BY [coloumns,…] ASC/DESC
	LIMIT 

**Functions**

SUM,AVG,COUNT

**JOIN more than two tables**

	SELECT [DISTINCT] …, …
	FROM [table]
	JOIN [table]
	ON <expr>
	JOIN [table]
	ON <expr>
	
**Import and export data‌**
Create table and import data:

	CREATE TABLE [table_name] (
	    longitude numeric(9,6),
	    latitude numeric(9,6),
	    street_number varchar(10),
	    street varchar(32),
	    unit varchar(7),
	    postcode varchar(5),
	    id integer CONSTRAINT new_york_key PRIMARY KEY
	);
	COPY new_york_addresses
	FROM '[path_to_file]'
	WITH (FORMAT CSV, HEADER);

Export Data

	COPY [table_name]
	TO '[Path_to_file]'
	WITH (FORMAT CSV, HEADER, DELIMITER ['|']);
																					
**Table design**

indexes: improve query speed.Primary key always has index.

	CREATE INDEX street_idx ON new_york_addresses (street);
Remove index:

	DROP INDEX
	
Consideration:
1. Look the documentation about indexes available
2. add indexes to columns use in table joins
3. add indexes to columns frequently used in WHERE clause
4. use EXPLAIN ANALYZE to test performance

[TODO]

**Ranking**

**Calculate date and time**	

Set Operators

Subqueries

**Common Table Expression**

**Views**
**Automating database actions**

Stored procedures

TODO []
**Data modification with INSERT, UPDATE, And DELETE**
Before modify database, back up it with:

CREATE TABLE [table__backup] AS
SELECT * FROM [table];

**UPDATE**
Update column record

	UPDATE table
	SET column = value
	WHERE criteria;

Update table 

	UPDATE table
	SET column = (SELECT column
	              FROM table_b
	              WHERE table.column = table_b.column)
	WHERE EXISTS (SELECT column
	              FROM table_b
	              WHERE table.column = table_b.column);

	UPDATE table
	SET column = table_b.column
	FROM table_b
	WHERE table.column = table_b.column;

### Workflow with a new Database
1. Know the columns
2. Know each column’s value type
3. Exam the nulls, missing value 
4. Know the relationship between tables
One to One, One to many

TODO
[ ] Difference among Mysql, Teradata and Postgresql

