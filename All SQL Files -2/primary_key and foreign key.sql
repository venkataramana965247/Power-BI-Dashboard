create database student_details;
-- primary key : no duplicates and no null values

create table courses(
	cid int primary key,
    cname varchar(20),
    cfee int
	);
    
insert into courses
values
(101,'python',5000),
(102,'java',4000),
(103,'ui',3000);

select * from courses;

-- foreign key : with duplicate and null values
-- this is the syntax and example of a foreign key....

create table students(
	sid int primary key,
    sname varchar(20),
    courseid int,
    foreign key students(courseid)
    references courses(cid)
    );
    
insert into students
values
(1,'A',101),
(2,'B',101),
(3,'C',101),
(4,'D',101),
(5,'E',102),
(6,'F',102),
(7,'G',103),
(8,'H',103);

insert into students(sid , sname)
values
(9,'I'),
(10,'J');

select * from students;

-- joins concepts : right join,left join

-- display student name and registered course names from both table ??

select s.sname ,c.cname
from students s 
join courses c
on 
s.courseid = c.cid;

-- display student name and registered course names from both table by using left join ??
select s.sname,c.cname
from students s
left join courses c
on
s.courseid = c.cid;

-- student enrolled for python course?

select s.sname,c.cname
from students s
join courses  c
on 
s.courseid = c.cid
where c.cname = 'python';


