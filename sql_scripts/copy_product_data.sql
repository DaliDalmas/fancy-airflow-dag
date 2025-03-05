drop table if exists  product_info;

create table product_info (
	product_id varchar,
	name varchar,
	price int,
	billing_cycle int
);

copy product_info (product_id, name, price, billing_cycle)
from '/Users/dalmasotieno/Documents/youtube/sqltos3/data/product_info.csv'
delimiter ','
csv header;

select * from public.product_info limit 5;


-- ------------------------------------------------------------------------

drop table if exists  customer_product;

create table customer_product (
	table_index int,
	customer_id varchar,
	product varchar,
	signup_date_time timestamp,
	cancel_date_time timestamp
);

copy customer_product (table_index, customer_id, product, signup_date_time, cancel_date_time)
from '/Users/dalmasotieno/Documents/youtube/sqltos3/data/customer_product.csv'
delimiter ','
csv header;

select * from public.customer_product limit 5;



