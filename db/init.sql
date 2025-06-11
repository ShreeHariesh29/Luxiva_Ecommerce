create database luxiva_ecommerce;

use luxiva_ecommerce;

create table product_items(
id INT auto_increment NOT NULL primary key,
name varchar(30),
discription text,
price int,
quantaty int,
rating int);

insert into product_items (name, discription, price, quantaty) values (
"POLO","Cotton round-neck t-shirt for daily wear.", 5000, 20);