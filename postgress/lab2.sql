-- 1. Insert personal data as new employee
INSERT INTO Employee VALUES ('Ayman', 'Osama', '102672', '2003-05-15', '123 fateh St. Tanta', 'M', 1200, '112233', 30);

-- 2. Insert friend data without salary or supervisor
INSERT INTO Employee VALUES ('hosny', 'zalat', '102660', '2006-08-20', '456 Giza', 'M', NULL, NULL, 30);

-- 3. Insert new department "DEPT IT"
INSERT INTO Department VALUES ('DEPT IT', 100, '112233', '2006-11-01');

-- 4a. Update Noha to be manager of department 100
UPDATE Department SET MGRSSN = '968574', MGRStartDate = '2006-11-01' WHERE DNum = 100;
-- 4b. Update your record to be department 20 manager (with current date as start date)
UPDATE Department SET MGRSSN = '102672', MGRStartDate = CURRENT_DATE WHERE DNum = 20;
UPDATE Employee SET Dno = 20 WHERE SSN = '102672';
-- 4c. Update friend to be supervised by you
UPDATE Employee SET Superssn = '102672' WHERE SSN = '102660';


-- 5. Delete Kamel Mohamed 
-- Update employees supervised by Kamel
UPDATE Employee SET Superssn = '102660' WHERE Superssn = '223344';
-- Update department manager (friend takes Kamel's position with current date)
UPDATE Department SET MGRSSN = '102660', MGRStartDate = CURRENT_DATE WHERE MGRSSN = '223344';
-- Delete from Works_for
DELETE FROM Works_for WHERE ESSN = '223344';
-- Delete dependents
DELETE FROM Dependent WHERE ESSN = '223344';
-- Delete employee
DELETE FROM Employee WHERE SSN = '223344';


-- 6. Upgrade salary by 20%
UPDATE Employee SET Salary = Salary * 1.2 WHERE SSN = '102672';



-- 1. Display all the employees Data
SELECT * FROM Employee;

-- 2. Display the employee First name, last name, Salary and Department number
SELECT Fname, Lname, Salary, Dno FROM Employee;

-- 3. Display all the projects names, locations and the department which is responsible about it
SELECT p.Pname, p.Plocation, d.Dname
FROM Project p
JOIN Department d ON p.Dnum = d.DNum;

-- 4. Display each employee full name and annual commission (10% of annual salary)
SELECT CONCAT(Fname, ' ', Lname) AS "Full Name",
(Salary * 12 * 0.10) AS "ANNUAL COMM"
FROM Employee
WHERE Salary IS NOT NULL;

-- 5. Display the employees Id, name who earns more than 1000 LE monthly
SELECT SSN, CONCAT(Fname, ' ', Lname) AS Name
FROM Employee
WHERE Salary > 1000;

-- 6. Display the employees Id, name who earns more than 10000 LE annually
SELECT SSN, CONCAT(Fname, ' ', Lname) AS Name
FROM Employee
WHERE (Salary * 12) > 10000;

-- 7. Display the names and salaries of the female employees
SELECT CONCAT(Fname, ' ', Lname) AS Name, Salary
FROM Employee
WHERE Sex = 'F';

-- 8. Display each department id, name which managed by a manager with id equals 968574
SELECT DNum, Dname
FROM Department
WHERE MGRSSN = '968574';

-- 9. Display the IDs, names and locations of the projects which controlled with department 10
SELECT Pnumber, Pname, Plocation
FROM Project
WHERE Dnum = 10;