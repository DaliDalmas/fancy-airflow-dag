
drop table if exists  customer_info;
create table customer_info (
	table_index int,
	customer_id varchar,
	age int,
	gender varchar
);

copy customer_info (table_index, customer_id, age, gender)
from '/Users/dalmasotieno/Documents/youtube/sqltos3/data/customer_info.csv'
delimiter ','
csv header;

select * from public.customer_info limit 5;

-- --------------------------------------------------------------------------

drop table if exists  customer_cases;
create table customer_cases (
	table_index int,
	case_id varchar,
	date_time timestamp,
	customer_id varchar,
	channel varchar,
	reason varchar
);

copy customer_cases (table_index, case_id, date_time, customer_id, channel, reason)
from '/Users/dalmasotieno/Documents/youtube/sqltos3/data/customer_cases.csv'
delimiter ','
csv header;

select * from public.customer_cases limit 5;
