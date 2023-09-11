CREATE database sept_database;
use sept_database;
CREATE TABLE sept_table_alpha (PrimaryID int not null auto_increment, username varchar(30) not null, password varchar(30) not null, element varchar(10) not null, age int not null, primary key(PrimaryID));
INSERT INTO sept_table_alpha(username, password, element, age)
VALUES('drowninginthewaves', 'help123', 'water', 22);
INSERT INTO sept_table_alpha(username, password, element, age)
VALUES('suffocatinginthestars', 'help234', 'light', 22);
INSERT INTO sept_table_alpha(username, password, element, age)
VALUES('ninjinsan', 'luoboxianshen', 'carrot', 4);

CREATE TABLE sept_table_beta (PrimaryID int not null auto_increment, playername varchar(22) not null, description text, fav_num int not null, primary key (PrimaryID));
INSERT INTO sept_table_beta (playername, description, fav_num)
VALUES('ginjo23', 'whatever is', 33)