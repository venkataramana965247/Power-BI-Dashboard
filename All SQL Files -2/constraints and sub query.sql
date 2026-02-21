create table voters(
	id int unique not null,
    name varchar(20) not null,
    age int not null check(age>=18),
    state varchar(20) default 'Telangana' check(state='Telangana')
    );
    
-- by using the constraints(UNIQUE, NOT NULL, CHECK ,DEFAULT) : 
--  1) How the constraints allows??
-- this is the one way :

insert into voters
values(101,'ram',22,'Telangana');

-- this is the another way :

insert into voters(id ,name ,age) values(102,"sitha",21);

-- this is the how the constraints doesn't allows the constraints:(we got an errors format of using constraints)
insert into voters values(103,"hain",24, 'Andhra'); -- we got check error
insert into voters(id,name,age) values(102,'harin',27);  -- we got duplicate error
insert into voters(id,name,age) values(104,26);   -- name not null
insert into voters(id,name,age) values(104,"hari",15);  -- we got error from the check constraints

-- sub query : it is a query written inside another query(always the first query will execute then main query) .

select max(age) from voters;
-- 		[or]
select max(age) from voters where age <= (select max(age) from voters);
select max(age) from voters where age < (select max(age) from voters);

create table employee(
	id int unique not null,
    name varchar(20) not null,
    salary int
    );
insert into employee
values
(1,'a',23000),
(2,'b',32000),
(3,'c',27000),
(4,'d',31000),
(5,'e',28000),
(6,'f',25000);

-- adding the one new col name as a dept_id :
alter table employee 
add dept_id int not null;

-- update the data into the dept_id :
update employee
set dept_id = 234
where id = 1;

update employee
set dept_id = 123
where id = 2;

update employee
set dept_id = 234
where id = 3;

update employee
set dept_id = 345
where id = 4;

update employee
set dept_id = 123
where id = 5;

update employee
set dept_id = 234
where id = 6;

select * from employee;

create table Department(
	dept_id int unique,
    dept_name varchar(20)
    );
insert into department
values 
(123,'IT'),
(234,'HR'),
(345,'sales');

select * from department;

-- by these two tables and written the query of the sub query??
select * from department where dept_name = 'HR';
select * from employee where dept_id=234;

-- sub query
select * from employee where dept_id = (select dept_id from department where dept_name = 'HR');
select * from employee where salary > (select avg(salary) from employee);