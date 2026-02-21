SELECT * FROM test.account;

-- this is the many choices programs using python with SQL : 
create table account(
	num int unique not null,
    name varchar(20),
    balance decimal(10,2)
    );
    
insert into account 
values
(101,"harish",1000),
(102,"ramana",2000),
(103,"prasad",30000),
(104,"sitha",5000),
(105,"geetha",9000);

select * from account;