# student-report-card-generator


sql source code
•	First create a first  table named student and insert the record in mysql
create table student (admno int (11) not null auto_increment, name varchar (30) default null, class varchar (15) default null, section varchar (10) default null, primary key (admno));

insert into student (admno, name, class, section) values (101, 'aryan’, ‘12', 'a'), (102, 'rukesh', '12', 'b');


•	Second create a second table named marks and insert the record in mysl.
create table marks (ad int(11)    default null ,phy int(3) default null,chem int(3) default null,math int(3) default null,eng int(3) default null,comp int(3) default null);

insert into marks(ad,   phy, chem, math, eng, comp) values(101,  67, 89, 90, 67, 90),(102, 67, 78, 56, 34, 45);
