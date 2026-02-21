select database() college;
use college;

create table product(id int,name varchar(20),quantity int,price double(9,2));
insert into product 
values
(101,"monitor",17,3500),
(102,"keyboard",12,450),
(103,"harddisk",15,5500),
(104,"Ram",32,2300),
(105,"monitor",8,20000),
(106,"mouse",54,1500),
(107,"keyboard",15,3000),
(108,"mouse",12,35000),
(109,"harddisk",5,8500);

truncate table product;
select * from product;

-- Extra examples in Arithmetic operators : +,-,*,/,%,...

select id,"Harddrive" as name from product where name = "harddisk";
select *,price-100 as detect_price from product where id = 101;
select * ,price + 25 as add_extra_price from product where id = 106;
select * , price-500 as decreased_price from product where id = 109;
select *,quantity-10 as decreased_quantity from product where  id = 106 and name = "mouse";
select *,quantity-5 as decreased_quantity from product where id = 105 and name = "monitor";
select * , quantity * 2 as double_of_quantity from product where id = 109 and name = "harddisk";

-- extra examples in Relational operators : <, >, <=,>=  = , !=...

select * from product where id = 103;
select * from product where quantity > 20 ;
select * from product where price = 3000;
select * from product where price <= 1000;

-- Extra examples in Logical Operators : and , or, not, in between....alter

select * from product where id between 103 and 107;
select * from product where id !=102 and id != 105 and id != 108 ;
select * from product where quantity > 20 and price < 7000;
select * from product where name != "monitor" and name != "keyboard" and name != "mouse";
select min(quantity) from product where price > 2000;

-- Extra examples in Like operator : % , _

select * from product where name like "m%";
select * from product where name like "_e%";
select * from product where length(name)= 5;
select * from product where min(quantity);
select min(quantity) from product ;
select min(quantity) from product where name like "m%" ;
select * from product where name like "m%" and quantity >= 10;
select * from product where name like "k%" and price < 1000;

-- Extra examples in Aggregate functions : min,max,sum,avg, count and length

select count(*) from product ;
select min(quantity) from product ;
select max(price) from product ;
SELECT COUNT(*) FROM product WHERE name = 'monitor' OR name = 'mouse';
SELECT COUNT(*) FROM product WHERE name IN ('monitor', 'mouse');
select * from product where name="monitor";
select min(price) from product where name = "monitor";
select max(price) from product where name = "keyboard" ;
select avg(price) from product where name = "mouse";

-- Extra examples in Order by : asc and desc orders 

select * from product order by name asc;
select * from product order by price desc; 
select * from product order by quantity desc;
select * from product where quantity >= 20 order by name ;
select * from product where quantity between 15 and 30 order by price desc;
use product;		

-- Extra examples in group by clause : the GROUP BY Clause is used to group rows that have the same values in one or more columns and apply aggregate funs on each group.
select * from product;
select count(id) from product;
select count(name) from product where name = 'mouse';
select count(name) from product where name = 'keyboard';
select count(name) from product where name = 'harddisk';
select name,count(*) from product group by name;
select name , sum(quantity) from product group by name;

-- Extra uses of group by and order by clauses :
select name , count(*) from product group by name order by name asc;

-- [or]

select name , count(*) from product group by name order by name ;
select name , count(*) from product group by name order by name desc;

-- Having clause : 
select name, count(name) from product group by name having name = 'mouse';
select name , count(name) from product group by name having count(name) >= 1 ;
select name , count(name) from product group by name having count(name) > 1 ;
select name , count(name) from product group by name having count(name) >= 1 order by count(name);
