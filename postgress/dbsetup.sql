
CREATE TABLE Department (
DName VARCHAR(50),
DNum INTEGER PRIMARY KEY,
MGRSSN VARCHAR(10),
MGRStartDate DATE
);

CREATE TABLE Employee (
Fname VARCHAR(50),
Lname VARCHAR(50),
SSN VARCHAR(10) PRIMARY KEY,
BDATE DATE,
Address VARCHAR(200),
Sex CHAR(1),
Salary INTEGER,
SuperSSN VARCHAR(10),
Dno INTEGER,
FOREIGN KEY (SuperSSN) REFERENCES Employee(SSN),
FOREIGN KEY (Dno) REFERENCES Department(DNum)
);

CREATE TABLE Project (
Pname VARCHAR(50),
Pnumber INTEGER PRIMARY KEY,
Plocation VARCHAR(100),
City VARCHAR(50),
Dnum INTEGER,
FOREIGN KEY (Dnum) REFERENCES Department(DNum)
);

CREATE TABLE Works_for (
ESSN VARCHAR(10),
Pno INTEGER,
Hours INTEGER,
PRIMARY KEY (ESSN, Pno),
FOREIGN KEY (ESSN) REFERENCES Employee(SSN),
FOREIGN KEY (Pno) REFERENCES Project(Pnumber)
);

CREATE TABLE Dependent (
ESSN VARCHAR(10),
Dependent_name VARCHAR(50),
Sex CHAR(1),
Bdate DATE,
PRIMARY KEY (ESSN, Dependent_name),
FOREIGN KEY (ESSN) REFERENCES Employee(SSN)
);


INSERT INTO Department VALUES ('DP1', 10, '223344', '2005-01-01');
INSERT INTO Department VALUES ('DP2', 20, '968574', '2006-03-01');
INSERT INTO Department VALUES ('DP3', 30, '512463', '2006-06-01');

INSERT INTO Employee VALUES ('Amr', 'Omran', '321654', '1963-09-14', '44 Hilopolis.Cairo', 'M', 2500, NULL, NULL);
INSERT INTO Employee VALUES ('Kamel', 'Mohamed', '223344', '1970-10-15', '38 Mohy el dien abo el Ezz St.Cairo', 'M', 1800, '321654', 10);
INSERT INTO Employee VALUES ('Noha', 'Mohamed', '968574', '1975-02-01', '55 Orabi St. El Mohandiseen .Cairo', 'F', 1600, '321654', 20);
INSERT INTO Employee VALUES ('Edward', 'Hanna', '512463', '1972-08-19', '18 Abaas El 3akaad St. Nasr City.Cairo', 'M', 1500, '321654', 30);
INSERT INTO Employee VALUES ('Ahmed', 'Ali', '112233', '1965-01-01', '15 Ali fahmy St.Giza', 'M', 1300, '223344', 10);
INSERT INTO Employee VALUES ('Hanaa', 'Sobhy', '123456', '1973-03-18', '38 Abdel Khalik Tharwat St. Downtown.Cairo', 'F', 800, '223344', 10);
INSERT INTO Employee VALUES ('Mariam', 'Adel', '669955', '1982-06-12', '269 El-Haram st. Giza', 'F', 750, '512463', 20);
INSERT INTO Employee VALUES ('Maged', 'Raoof', '521634', '1980-04-06', '18 Kholosi st.Shobra.Cairo', 'M', 1000, '968574', 30);
ALTER TABLE Department ADD FOREIGN KEY (MGRSSN) REFERENCES Employee(SSN);

INSERT INTO Project VALUES ('AL Solimaniah', 100, 'Cairo_Alex Road', 'Alex', 10);
INSERT INTO Project VALUES ('Al Rabwah', 200, '6th of October City', 'Giza', 10);
INSERT INTO Project VALUES ('Al Rawdah', 300, 'Zaied City', 'Giza', 10);
INSERT INTO Project VALUES ('Al Rowad', 400, 'Cairo_Faiyom Road', 'Giza', 20);
INSERT INTO Project VALUES ('Al Rehab', 500, 'Nasr City', 'Cairo', 30);
INSERT INTO Project VALUES ('Pitcho american', 600, 'Maady', 'Cairo', 30);
INSERT INTO Project VALUES ('Ebad El Rahman', 700, 'Ring Road', 'Cairo', 20);

INSERT INTO Works_for VALUES ('223344', 100, 10);
INSERT INTO Works_for VALUES ('223344', 200, 10);
INSERT INTO Works_for VALUES ('223344', 300, 10);
INSERT INTO Works_for VALUES ('112233', 100, 40);
INSERT INTO Works_for VALUES ('968574', 400, 15);
INSERT INTO Works_for VALUES ('968574', 700, 15);
INSERT INTO Works_for VALUES ('968574', 300, 10);
INSERT INTO Works_for VALUES ('669955', 400, 20);
INSERT INTO Works_for VALUES ('223344', 500, 10);
INSERT INTO Works_for VALUES ('669955', 700, 7);
INSERT INTO Works_for VALUES ('669955', 300, 10);
INSERT INTO Works_for VALUES ('512463', 500, 10);
INSERT INTO Works_for VALUES ('512463', 600, 25);
INSERT INTO Works_for VALUES ('521634', 500, 10);
INSERT INTO Works_for VALUES ('521634', 600, 20);
INSERT INTO Works_for VALUES ('521634', 300, 6);
INSERT INTO Works_for VALUES ('521634', 400, 4);

INSERT INTO Dependent VALUES ('112233', 'Hala Saied Ali', 'F', '1970-10-18');
INSERT INTO Dependent VALUES ('223344', 'Ahmed Kamel Shawki', 'M', '1998-03-27');
INSERT INTO Dependent VALUES ('223344', 'Mona Adel Mohamed', 'F', '1975-04-25');
INSERT INTO Dependent VALUES ('321654', 'Ramy Amr Omran', 'M', '1990-01-26');
INSERT INTO Dependent VALUES ('321654', 'Omar Amr Omran', 'M', '1993-03-30');
INSERT INTO Dependent VALUES ('321654', 'Sanaa Gawish', 'F', '1973-05-16');
INSERT INTO Dependent VALUES ('512463', 'Sara Edward', 'F', '2001-09-15');
INSERT INTO Dependent VALUES ('512463', 'Nora Ghaly', 'F', '1976-06-22');