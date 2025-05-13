# MySQL to SQL Server transition guide

MySQL and SQL Server has got some shuttle diffs in their syntax :)
Lem'me point some of it out for ya!

## Core navigation

- Show databases

```sql
select * from sys.databases;
```

- enter into a database

```sql
use your_database_name;
```

> here your_database_name is the name of the database you want to enter.

- Show tables

```sql
select * from sys.tables;
```

- describe table

```sql
exec sp_help 'table_name';
```

> here table_name is the name of the table you want to describe.

---

## Differences

- No natural join! Only Join :(
- No space after a function and parenthesis
- No space after comma in group by or other stuff
- `IF NOT EXISTS` is not directly supported
- Replace `limit` with ‌‌‌‌‌`top‌‌‍`

| MySQL                          | SQL Server                   |
| ------------------------------ | ---------------------------- |
| `SELECT * FROM table LIMIT 5;` | `SELECT TOP 5 * FROM table;` |

For example, to get the first 10 rows from a table named `student`, you would write:

```sql
SELECT TOP 10 * FROM student;
```

- SQL Server **only uses single quotes** for string literals.

```sql
-- Correct in SQL Server
WHERE name = 'Alice'
```

- AUTO INCREMENT vs IDENTITY

| MySQL                               | SQL Server                         |
| ----------------------------------- | ---------------------------------- |
| `id INT AUTO_INCREMENT PRIMARY KEY` | `id INT IDENTITY(1,1) PRIMARY KEY` |

- Functions

| Purpose       | MySQL          | SQL Server                |
| ------------- | -------------- | ------------------------- |
| Current date  | `CURDATE()`    | `GETDATE()`               |
| String length | `LENGTH()`     | `LEN()`                   |

- Row value constructor won't work

```sql
select * from student
where (ID,name) in (select ID,name from student
 where name='Duan');
```

---

## Examples

- Find student names and the number of law courses taken for students who have taken at least half of the available law courses. (These courses are named things like ‘Tort Law’ or ‘Environmental Law’).

```sql
select name, count(*)
from student as st
join takes as tt
on st.ID = tt.ID
where tt.course_id in (
 select course_id
    from course
    where title like '%Law%'
)
group by st.ID,st.name
having count(*) > (
 select count(*)/2
    from course
    where title like '%Law%'
);
```

- Find the rank and name of the 10 students who earned the most A grades (A-, A, A+). Use alphabetical order by name to break ties. Note: the browser SQLite does not support window functions.

```sql
select top 10 row_number() over(order by P.cnt desc,P.name) as rnk, P.name from ( 
 select name, count(*) as cnt
 from student S
 join takes T on S.ID = T.ID
 where T.grade in ('A+', 'A', 'A-')
 group by T.ID,S.name
    ) as P
order by P.cnt desc,P.name;
```

> In large university dataset, you will get something like,
>
> - 1 Neuhold
> - 2 Greene
> - 3 Hons
> - 4 Lepp
> - 5 Lingamp
> - 6 Mandviwall
> - 7 Drig
> - 8 Fabregas
> - 9 Haigh
> - 10 Heilprin
