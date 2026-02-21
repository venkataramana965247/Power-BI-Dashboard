
create database bankdetails;
create table account(num int,name varchar(20),balance int,age int,location varchar(20),type varchar(20));

insert into account values(1,"A",5000,23,"hyd","savings");

insert into account(num ,name ,balance ,location ,type) values(2,"B",7000,"pune","current");

insert into account(num ,name ,balance,age ,type) values(3,"c",6000,27,"salary");

insert into account values(4,"D",9000,28,"hyd","savings");
insert into account values(5,"E",6500,29,"pune","savings");

insert into account(num ,name ,age ,location,type) values(6,"F",28,"bnglr","current");

select * from account;

select num,balance 
from account;

UPDATE account
SET age = 30
WHERE num = 2
LIMIT 1;

UPDATE account
SET location = "VZM"
WHERE num = 3
LIMIT 1;

UPDATE account
SET balance = 2500
WHERE num = 6
LIMIT 1;

DELETE FROM account
WHERE num = 6
  AND name = 'F'
  AND age = 28
  AND location = 'bnglr'
  AND type = 'current'
LIMIT 1;

SELECT balance - 2000
FROM account
WHERE num = 4;

UPDATE account
SET type = 'current'
WHERE num = 1
LIMIT 1;

SELECT balance - 3000 AS new_balance
FROM account
WHERE num = 3;

DELETE FROM account
WHERE type = 'savings'
LIMIT 1000;

select * from account;



