--1
-- select Dnum, Dname, MGRSSN, Fname || ' ' || Lname as name
-- from Department inner join Employee on MGRSSN = SSN

--2
-- select Dname, Pname
-- from Project as p inner join Department as d on p.Dnum = d.DNum

--3
-- select Fname || ' ' || Lname as Name, ESSN, Dependent_name, d.Sex, d.Bdate
-- from Dependent as d join Employee on ESSN = SSN

--4
-- select dependent_name, d.Sex
-- from Dependent as d join Employee as e on ESSN=SSN
-- where d.Sex = 'F' and e.Sex = 'F'
-- union
-- select dependent_name, d.Sex
-- from Dependent as d join Employee as e on ESSN=SSN
-- where d.Sex = 'M' and e.Sex = 'M'

--5
-- select Pnumber as id, Pname, Plocation, City
-- from Project
-- where City = 'Cairo' or City = 'Alex'

--6
-- select Pnumber as id, Pname, Plocation, City, Dnum
-- from Project
-- where Pname ilike 'a%'

--7
-- select *
-- from Employee
-- where Dno = 30 and salary between 1000 and 2000

--8
-- select Fname || ' ' || Lname as name
-- from employee as e join works_for  as w on e.ssn = w.essn
-- join project as p on w.Pno = p.pnumber
-- where p.pname = 'Al Rabwah' and w.Hours >= 10 and e.dno = 10

--9
-- select Fname || ' ' || Lname as name
-- from employee
-- where superssn = (
-- 					select ssn from employee 
-- 				  	where Fname = 'Kamel' and Lname ='Mohamed'
-- 				 )

--10
-- select p.Pname, sum(w.Hours)
-- from Project as p join works_for as w on p.Pnumber = w.pno
-- group by p.pname

--11
-- select p.Pname, Fname || ' ' || Lname as name
-- from employee as e join works_for  as w on e.ssn = w.essn
-- join project as p on w.Pno = p.pnumber
-- order by P.Pname, Fname

--12
-- select *
-- from Department
-- where dnum = (
-- 				select dno from employee
-- 				where ssn = (select min(ssn) from employee)
-- )

--13
-- select dname, min(salary), avg(salary), max(salary) 
-- from department join employee on dno = dnum
-- group by dname

--14
-- select Fname || ' ' || Lname as name
-- from employee join Department on ssn = mgrssn
-- where mgrssn not in (
-- 					select distinct Essn from dependent
-- 				)

--15
-- select dnum, dname, count(ssn)
-- from department join employee on dno = dnum
-- group by dnum, dname
-- having avg(salary) < (select avg(e.salary) from employee as e)

--16
-- select Fname || ' ' || Lname as name, pname, dno
-- from employee join works_for on ssn = essn
-- join project on pnumber = pno
-- order by dno, lname, fname

--17
-- select pnumber, dname, lname ,address, bdate
-- from project as p join department as d on d.dnum = p.dnum
-- join employee on ssn = mgrssn
-- where city = 'Cairo'