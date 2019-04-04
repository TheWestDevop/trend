create table country(id int primary key auto_increment,
name varchar(500));

create table state(id int primary key auto_increment,
name varchar(500),
cid int);

create table town(id int primary key auto_increment,
name varchar(500),
sid int);

create table sources(id int primary key auto_increment,
name varchar(200),
url text,
cid int,
status int);

create table articles(id int primary key auto_increment,
title varchar(255),
summary text,
shortdesc text,
content longtext,
sid int,
status int,
author varchar(200),
pubdate datetime);
create table user(id int primary key auto_increment,username varchar(10),
password varchar(200),secret varchar(200),isemailverified int,
isphoneverified int,status int,
createdate datetime);
create table profile(id int primary key auto_increment,uid int,firstname varchar(100),
lastname varchar(100),othername varchar(100),email varchar(100),
telephone varchar(50),address varchar(100),address2 varchar(100),city int,
state int,country int,postalcode varchar(20),
createdate datetime);

