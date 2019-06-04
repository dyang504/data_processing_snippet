## The Cheat Sheet of SQL And Deal with database
### Cheat Sheet
**Key WORDS**

`CASE` USAGE: 1. Reclassifying values, Add new category column;2. Exclude/clean unwanted values, a filter;3.`CASE` can use with other functions like `SUM`

**Basic Query Pattern**

	SELECT [DISTINCT] …, …
	FROM [table]
	WHERE <expr>
	GROUP BY [coloumns,…]
	HAVING <expr>
	ORDER BY [coloumns,…] ASC/DESC
	LIMIT [num] OFFSET [num];

**Functions**

SUM,AVG,COUNT

**JOIN more than two tables**

	SELECT [DISTINCT] …, …
	FROM [table]
	JOIN [table]
	ON <expr>
	JOIN [table]
	ON <expr>;
	
**Import and export data‌**
Create table and import data:

	CREATE TABLE [table_name] (
	    [columns type,…]
	    id integer CONSTRAINT [constrain_name] PRIMARY KEY
	);
	COPY [table_name]
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

	DROP INDEX ;
	
Consideration:
1. Look the documentation about indexes available
2. add indexes to columns use in table joins
3. add indexes to columns frequently used in WHERE clause
4. use EXPLAIN ANALYZE to test performance         

**Common Table Expression**

	WITH [new_table_name] AS (
		SELECT [column1,..columnN]
		FROM [table_name]
	)
	SELECT [column1,..columnN]
	FROM [table_name]
	JOIN [table2] ON <expr>
	…

**Views**
reuse queries; insert, update, deleting data.

	CREATE [OR REPLACE] VIEW [view_name] AS
		SELECT [columns,…]
		FROM [table_name]
		…
**Automating database actions**
Stored procedures

**Data modification with UPDATE**
Before modify database, back up it with:

	CREATE TABLE [table__backup] AS
	SELECT * FROM [table];

**UPDATE**
Update table record

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

[TODO]
Ranking
Set Operators  

