CREATE DATABASE first_database;
USE first_database;
CREATE TABLE first_table (UserID int NOT NULL AUTO_INCREMENT, Usernames varchar(15), Passwords varchar(20), primary key(UserID));
INSERT INTO first_table (Usernames, Passwords)
VALUES ('primero', 'primeropassword');
DELETE FROM first_table WHERE UserID=2;