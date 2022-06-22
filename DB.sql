CREATE DATABASE challenge;

USE challenge;

CREATE TABLE us_sec (
name_alias VARCHAR(45) PRIMARY KEY NOT NULL,
pass VARCHAR(32) NOT NULL,
create_time TIMESTAMP ,
status BOOLEAN 
);

CREATE TABLE g_sec (
id VARCHAR(45) NOT NULL,
name_gs VARCHAR(45) NOT NULL,
description_gs VARCHAR(255) NOT NULL,
FOREIGN KEY (id) REFERENCES us_sec(name_alias)
);

CREATE TABLE levelacc(
idacc VARCHAR(45) NOT NULL,
nameacc VARCHAR(45) NOT NULL,
FOREIGN KEY (idacc) REFERENCES g_sec(id)
);