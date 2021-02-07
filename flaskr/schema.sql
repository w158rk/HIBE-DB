DROP TABLE IF EXISTS user;


CREATE TABLE user (
	id integer PRIMARY KEY AUTOINCREMENT,
	name varchar NOT NULL UNIQUE,
	x varchar(64),
	host varchar NOT NULL,
	port integer NOT NULL,
	pk varchar,
	parent integer
);

-- test data

INSERT INTO user (name, host, port) VALUES ("Server1", "localhost", 20001);
INSERT INTO user (name, x, host, port) VALUES ("Server2", "abcaddf123541", "localhost", 20002);
INSERT INTO user (name, host, port) VALUES ("Server3", "localhost", 20003);
INSERT INTO user (name, host, port) VALUES ("Server4", "localhost", 20004);
INSERT INTO user (name, host, port) VALUES ("Server5", "localhost", 20005);
