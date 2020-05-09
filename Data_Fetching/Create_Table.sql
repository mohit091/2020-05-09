create database etl; ## craete database etl
\connect etl; ## connect to database etl
CREATE TABLE EVENTS (ID INT,EVENT_NAME VARCHAR, PEOPLE_COUNT BIGINT,PRIMARY KEY (ID));
