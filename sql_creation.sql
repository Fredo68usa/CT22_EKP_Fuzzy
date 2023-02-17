DROP TABLE currentSQLs;
CREATE TABLE currentSQLs(
hash varchar(32) PRIMARY KEY,
SQL varchar(500),
hashSim varchar(32),
status varchar(20),
score INT,
frequency INT
);

