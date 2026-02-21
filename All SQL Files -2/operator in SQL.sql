SELECT * FROM college.emp;

USE college;

-- Relational operators : 
-- (>,<,>=,<=,=,!=)

select * from emp where id=1;
select * from emp where loc="hyd";
select * from emp where dept!="IT";
select * from emp where age >= 27;
select * from emp where salary < 40000;

-- logical operators : and , or , not , in , between 
select * from emp where id=1 and id=5;
select * from emp where id in (1,5);

select * from emp where age >=25 and age<=27;
-- or 
select * from emp where age between 25 and 27;

select * from emp where id not in (1,5);
select * from emp where age not between 25 and 27;

-- like operator : %(percentage) and _(underscore)
select * from emp where name like "a%";
-- or
select * from emp where name like "A%";

select * from emp where name like "%i";

select * from emp where name like "____";
select * from emp where name like "___";
select * from emp where name like "_____";

select * from emp where name like "_a%";

-- Aggregate functions : always returns single value results
-- count(),sum(),avg(),min(),max()

select count(*) from emp;
select count(*) as Total_num_of_records from emp;

select min(age) from emp;
select max(age) from emp;
select avg(salary) from emp;

select count(id) from emp where loc="hyd";
select count(*) from emp where loc="hyd";
select min(salary) from emp where dept="IT";
select sum(salary) from emp where dept!="IT";

select count(name) from emp where name like "H%";

-- clauses in SQL : where,order by ,group by, having 
-- 1) where : it is used to filter records and select only those rows that satisfy a given condition.
-- 2) order by : is used to display information in sorted(asc(ascending) OR (desc(descending) order) 
-- ex :
select * from emp order by name;
-- OR 
select * from emp order by name ASC;

select * from emp order by name desc;

-- order by and where clauses : (FIrst -where , Second - order by ) => first filter then sort

select * from emp where dept="IT";
select * from emp where dept="IT" order by name asc ;
select * from emp where dept="IT" order by name desc ;

select * from emp where loc = "hyd" order by age asc;
select * from emp where loc = "hyd" order by age desc;


