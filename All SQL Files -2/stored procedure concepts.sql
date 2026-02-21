create database test;

show databases;
use test;

create table account(
	num int primary key,
    name varchar(20),
    balance decimal(10,2)
    );
    
select * from account;

-- creation of a stored procedure:
-- 1)Example :

delimiter $$
create procedure insert_account(
	in p_num int,
    in p_name varchar(20),
    in p_balance decimal(10,2)
    )
    begin
    insert into account values(p_num,p_name,p_balance);
    end $$
Delimiter ;

call insert_account(101,'amar',50000);
call insert_account(102,'anil',40000);
call insert_account(103,'koila',30000);

select * from account;

-- 2) Example:

delimiter $$
create procedure deposite_amount(
	in p_num int,
    in p_name varchar(20),
    in p_amount decimal(10,2)
    )
	begin
    update account set balance = balance + p_amount where num = p_num;
    end $$
	delimiter ;
    
call deposite_amount(101,'amar',20000); -- updating of the amar as deposit amount.

select * from account;

-- Extra examples of procedure concept :?
-- 1) write procedure to update name by giving(num , new_name)

DELIMITER $$

CREATE PROCEDURE update_name
(
    IN p_num INT,
    IN p_new_name VARCHAR(20)
)
BEGIN
    UPDATE account
    SET name = p_new_name
    WHERE num = p_num;
END $$

DELIMITER ;

CALL update_name(101, 'A');

SELECT * FROM account;

-- 2) write procedure to delete record by giving num.alter

DELIMITER $$

CREATE PROCEDURE delete_record(
    IN p_num INT
)
BEGIN
    DELETE FROM account
    WHERE num = p_num;
END $$

DELIMITER ;

CALL delete_record(101);

select * from account;
	
