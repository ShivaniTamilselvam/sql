--create table Patient(Pid int(10),Name varchar(20),Health varchar(20),Gender char,City varchar(20));  
--insert into Patient values(113,'Nithya','stomach ache','F','Pondy');
select Pid,Health from Patient where city='chennai';
