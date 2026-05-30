CREATE TABLESPACE academy_data LOCATION 'C:/PostgreSQL/data3/tablespace';

SELECT *
FROM pg_tablespace
WHERE spcname = 'academy_data';

CREATE DATABASE Academy
    OWNER = postgres
    ENCODING = 'UTF8'
    TABLESPACE = academy_data;

CREATE TABLE Departments (
    Id SERIAL PRIMARY KEY,
    Financing MONEY NOT NULL DEFAULT 0::money CHECK (Financing >= 0::money),
    Name VARCHAR(100) NOT NULL UNIQUE CHECK (Name <> '')
);

CREATE TABLE Faculties (
    Id SERIAL PRIMARY KEY,
    Dean VARCHAR(100) NOT NULL CHECK (Dean <> ''),
    Name VARCHAR(100) NOT NULL UNIQUE CHECK (Name <> '')
);

CREATE TABLE Groups (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL UNIQUE CHECK (Name <> ''),
    Rating INTEGER NOT NULL CHECK (Rating BETWEEN 0 AND 5),
    Year INTEGER NOT NULL CHECK (Year BETWEEN 1 AND 5)
);

CREATE TABLE Teachers (
    Id SERIAL PRIMARY KEY,
    EmploymentDate DATE NOT NULL CHECK (EmploymentDate >= '1990-01-01'),
    IsAssistant BOOLEAN NOT NULL DEFAULT FALSE,
    IsProfessor BOOLEAN NOT NULL DEFAULT FALSE,
    Name VARCHAR(255) NOT NULL CHECK (Name <> ''),
    Position VARCHAR(255) NOT NULL CHECK (Position <> ''),
    Premium MONEY NOT NULL DEFAULT 0::money CHECK (Premium >= 0::money),
    Salary MONEY NOT NULL CHECK (Salary > 0::money),
    Surname VARCHAR(255) NOT NULL CHECK (Surname <> '')
);


INSERT INTO Departments (Financing, Name) VALUES
(100000.50::money, 'Кафедра математики и информатики'),
(150000.00::money, 'Кафедра физики и астрономии'),
(85000.75::money, 'Кафедра химии и биологии'),
(200000.00::money, 'Кафедра иностранных языков'),
(75000.25::money, 'Кафедра истории и философии');

INSERT INTO Faculties (Dean, Name) VALUES
('Иванов И.И.', 'Факультет точных наук'),
('Петров П.П.', 'Факультет естественных наук'),
('Сидоров С.С.', 'Гуманитарный факультет'),
('Козлова К.К.', 'Факультет иностранных языков'),
('Николаев Н.Н.', 'Исторический факультет');


INSERT INTO Groups (Name, Rating, Year) VALUES
('М-101', 5, 1),
('М-201', 4, 2),
('Ф-101', 3, 1),
('ХБ-301', 5, 3),
('ИФ-401', 2, 4),
('ИЯ-201', 4, 2),
('Ист-301', 3, 3);


INSERT INTO Teachers (
    EmploymentDate, IsAssistant, IsProfessor, Name, Position, Premium, Salary, Surname
) VALUES
('1995-03-15', FALSE, TRUE, 'Алексей', 'Профессор', 15000::money, 80000::money, 'Сидоров'),
('2005-09-01', TRUE, FALSE, 'Мария', 'Ассистент', 5000::money, 40000::money, 'Козлова'),
('2010-08-20', FALSE, FALSE, 'Дмитрий', 'Старший преподаватель', 8000::money, 55000::money, 'Николаев'),
('1998-02-10', FALSE, TRUE, 'Елена', 'Профессор', 20000::money, 90000::money, 'Иванова'),
('2015-06-12', TRUE, FALSE, 'Андрей', 'Ассистент', 6000::money, 38000::money, 'Петров'),
('2002-04-25', FALSE, FALSE, 'Ольга', 'Доцент', 12000::money, 65000::money, 'Смирнова'),
('2020-09-01', TRUE, FALSE, 'Иван', 'Ассистент', 4000::money, 35000::money, 'Васильев'),
('1992-11-05', FALSE, TRUE, 'Наталья', 'Профессор', 25000::money, 95000::money, 'Федорова'),
('2018-07-18', FALSE, FALSE, 'Сергей', 'Преподаватель', 7000::money, 48000::money, 'Морозов'),
('2008-03-30', FALSE, FALSE, 'Анна', 'Старший преподаватель', 9000::money, 60000::money, 'Павлова');


SELECT Name, Financing, Id
FROM Departments;

SELECT
    Groups.Name AS "Название группы",
    Groups.Rating AS "Рейтинг"
FROM Groups;


SELECT
    Surname AS "Фамилия",
    ROUND(
        (Premium::decimal / NULLIF(Salary::decimal, 0)) * 100,
        2
    ) AS "Процент надбавки от ставки (%)",
    ROUND(
        (Salary::decimal / NULLIF((Salary + Premium)::decimal, 0)) * 100,
        2
    ) AS "Процент ставки от общей суммы (%)"
FROM Teachers;

SELECT FORMAT('The dean of faculty %s is %s', Name, Dean) AS "Faculty Information"
FROM Faculties;

SELECT Surname
FROM Teachers
WHERE IsProfessor = TRUE AND Salary::numeric > 1050;


SELECT Name
FROM Departments
WHERE Financing::numeric < 11000 OR Financing::numeric > 25000;

SELECT Name
FROM Faculties
WHERE Name != 'Факультет точных наук';

SELECT Surname, Position
FROM Teachers
WHERE IsProfessor = FALSE;

SELECT Surname, Position, Salary, Premium
FROM Teachers
WHERE Position = 'Ассистент' AND Premium::numeric BETWEEN 1600 AND 5500;

SELECT Surname, Salary
FROM Teachers
WHERE Position = 'Ассистент';

SELECT Surname, Position
FROM Teachers
WHERE EmploymentDate < '2000-01-01';

SELECT Name AS "Name of Department"
FROM Departments
WHERE Name < 'Кафедра физики и астрономии'
ORDER BY Name;


SELECT Surname
FROM Teachers
WHERE Position = 'Ассистент'
  AND (Salary::numeric + Premium::numeric) <= 120000;

SELECT Name
FROM Groups
WHERE Year = 2
  AND Rating BETWEEN 2 AND 4;

SELECT Surname
FROM Teachers
WHERE Position = 'Ассистент'
  AND (Salary::numeric < 55000 OR Premium::numeric < 20000);

-------------------------------------------------------------------------------
CREATE TABLE Curators (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR NOT NULL CHECK (Name <> ''),
    Surname VARCHAR NOT NULL CHECK (Surname <> '')
);

CREATE TABLE Faculties_new (
    Id SERIAL PRIMARY KEY,
    Financing MONEY NOT NULL DEFAULT 0::money CHECK (Financing >= 0::money),
    Name VARCHAR(100) NOT NULL UNIQUE CHECK (Name <> '')
);

CREATE TABLE Departments_new (
    Id SERIAL PRIMARY KEY,
    Financing MONEY NOT NULL DEFAULT 0::money CHECK (Financing >= 0::money),
    Name VARCHAR(100) NOT NULL UNIQUE CHECK (Name <> ''),
    FacultyId INT NOT NULL,
    FOREIGN KEY (FacultyId) REFERENCES Faculties_new(Id)
);

CREATE TABLE Teachers_new (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR NOT NULL CHECK (Name <> ''),
    Salary MONEY NOT NULL CHECK (Salary > 0::money),
    Surname VARCHAR NOT NULL CHECK (Surname <> '')
);

CREATE TABLE Groups_new (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(10) NOT NULL UNIQUE CHECK (Name <> ''),
    Year INT NOT NULL CHECK (Year BETWEEN 1 AND 5),
    DepartmentId INT NOT NULL,
    FOREIGN KEY (DepartmentId) REFERENCES Departments_new(Id)
);

CREATE TABLE Subjects (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL UNIQUE CHECK (Name <> '')
);

CREATE TABLE Lectures (
    Id SERIAL PRIMARY KEY,
    LectureRoom VARCHAR NOT NULL CHECK (LectureRoom <> ''),
    SubjectId INT NOT NULL,
    TeacherId INT NOT NULL,
    FOREIGN KEY (SubjectId) REFERENCES Subjects(Id),
    FOREIGN KEY (TeacherId) REFERENCES Teachers_new(Id)
);

CREATE TABLE GroupsCurators (
    Id SERIAL PRIMARY KEY,
    CuratorId INT NOT NULL,
    GroupId INT NOT NULL,
    FOREIGN KEY (CuratorId) REFERENCES Curators(Id),
    FOREIGN KEY (GroupId) REFERENCES Groups_new(Id)
);

CREATE TABLE GroupsLectures (
    Id SERIAL PRIMARY KEY,
    GroupId INT NOT NULL,
    LectureId INT NOT NULL,
    FOREIGN KEY (GroupId) REFERENCES Groups_new(Id),
    FOREIGN KEY (LectureId) REFERENCES Lectures(Id)
);

begin;
INSERT INTO Faculties_new (Name)
SELECT Name FROM Faculties;
DROP TABLE Faculties;
ALTER TABLE Faculties_new RENAME TO Faculties;

INSERT INTO Departments_new (Financing, Name, FacultyId)
SELECT
    Financing,
    Name,
    1 AS FacultyId 
FROM Departments;
DROP TABLE Departments;
ALTER TABLE Departments_new RENAME TO Departments;

INSERT INTO Teachers_new (Name, Salary, Surname)
SELECT Name, Salary, Surname
FROM Teachers;
DROP TABLE Teachers;
ALTER TABLE Teachers_new RENAME TO Teachers;

INSERT INTO Groups_new (Name, Year, DepartmentId)
SELECT
    Name,
    Year,
    1 AS DepartmentId  
FROM Groups;
DROP TABLE Groups;
ALTER TABLE Groups_new RENAME TO Groups;
COMMIT;


INSERT INTO Curators (Name, Surname)
VALUES
    ('Анна', 'Смирнова'),
    ('Дмитрий', 'Иванов'),
    ('Елена', 'Петрова'),
    ('Сергей', 'Николаев'),
    ('Ольга', 'Козлова');

INSERT INTO Subjects (Name)
VALUES
    ('Высшая математика'),
    ('Физика'),
    ('Химия'),
    ('Биология'),
    ('Иностранный язык'),
    ('История'),
    ('Философия'),
    ('Программирование');

INSERT INTO Lectures (LectureRoom, SubjectId, TeacherId)
VALUES
    ('301', 1, 1),  
    ('302', 2, 2), 
    ('401', 3, 3),  
    ('205', 4, 4),  
    ('101', 5, 5),  
    ('310', 6, 6), 
    ('415', 7, 7), 
    ('501', 8, 8),  
    ('301', 1, 9),  
    ('205', 5, 10); 

SELECT Id AS CuratorId, Name, Surname FROM Curators;
SELECT Id AS GroupId, Name FROM Groups;

INSERT INTO GroupsCurators (CuratorId, GroupId)
VALUES
    (1, 1), 
    (2, 2), 
    (3, 3),  
    (4, 4),  
    (5, 5);  

SELECT Id AS GroupId, Name FROM Groups;
SELECT Id AS LectureId, LectureRoom FROM Lectures;

SELECT Id, Name FROM Faculties;

INSERT INTO Departments (Financing, Name, FacultyId)
VALUES
    (300000::money, 'Кафедра математического анализа', 1),
    (250000::money, 'Кафедра алгебры и геометрии', 1),
    (280000::money, 'Кафедра теоретической физики', 2),
    (220000::money, 'Кафедра экспериментальной физики', 2),
    (180000::money, 'Кафедра органической химии', 2),
    (160000::money, 'Кафедра неорганической химии', 2),
    (200000::money, 'Кафедра общей психологии', 3),
    (170000::money, 'Кафедра прикладной математики и программирования', 1),
    (150000::money, 'Китайский язык', 4),
    (140000::money, 'кафедра отечественной и всеобщей истории', 5);
SELECT FacultyId, Name  FROM  Departments

INSERT INTO Groups (Name, Year, DepartmentId)
VALUES
    ('М-111', 2, 1), 
    ('ПР-211', 2, 1), 
    ('АЛГ-111', 1, 1),
    ('ФИЭ-111', 1, 2),
    ('ФИТ-111', 1, 2),
    ('ОР-111', 1, 2),  
    ('Х-211', 2, 2),  
    ('К-311', 3, 4),  
    ('ПС-211', 2, 3),
    ('Ист-311', 3, 5); 

INSERT INTO GroupsCurators (CuratorId, GroupId)
VALUES
    (1, 1),  
    (2, 2),  
    (3, 3), 
    (4, 4),  
    (5, 5);  

SELECT Id AS GroupId, Name FROM Groups;
SELECT Id AS LectureId, LectureRoom FROM Lectures;

INSERT INTO GroupsLectures (GroupId, LectureId)
VALUES
    (1, 1), 
    (1, 5),  
    (2, 1),  
    (2, 6),  
    (3, 2),  
    (4, 3),  
    (5, 4), 
    (6, 7), 
    (7, 8),
    (21, 9), 
 	(22, 10),
	(23, 11),
	(24, 12),
	(25, 13),
	(26, 14),
	(28, 15),
	(29, 16),
	(30, 17);




SELECT
    t.Id AS "ID преподавателя",
    t.Name AS "Имя преподавателя",
    t.Surname AS "Фамилия преподавателя",
    g.Id AS "ID группы",
    g.Name AS "Название группы",
    g.Year AS "Курс"
FROM Teachers t
CROSS JOIN Groups g
ORDER BY t.Surname, g.Name;

UPDATE Faculties
SET Financing = ROUND((random() * 300000 + 30000) / 1000) * 1000::money;


SELECT DISTINCT f.Name AS "Название факультета"
FROM Faculties f
JOIN Departments d ON f.Id = d.FacultyId
WHERE d.Financing > f.Financing
ORDER BY f.Name;

SELECT
    c.Surname AS "Фамилия куратора",
    g.Name AS "Название группы"
FROM Curators c
JOIN GroupsCurators gc ON c.Id = gc.CuratorId
JOIN Groups g ON gc.GroupId = g.Id
ORDER BY c.Surname, g.Name;

SELECT DISTINCT
    t.Name AS "Имя преподавателя",
    t.Surname AS "Фамилия преподавателя"
FROM Teachers t
JOIN Lectures l ON t.Id = l.TeacherId
JOIN GroupsLectures gl ON l.Id = gl.LectureId
JOIN Groups g ON gl.GroupId = g.Id
WHERE g.Name = 'М-201'
ORDER BY t.Surname, t.Name;

SELECT DISTINCT
    t.Surname AS "Фамилия преподавателя",
    f.Name AS "Название факультета"
FROM Teachers t
JOIN Lectures l ON t.Id = l.TeacherId
JOIN GroupsLectures gl ON l.Id = gl.LectureId
JOIN Groups g ON gl.GroupId = g.Id
JOIN Departments d ON g.DepartmentId = d.Id
JOIN Faculties f ON d.FacultyId = f.Id
ORDER BY t.Surname, f.Name;

SELECT
    d.Name AS "Название кафедры",
    g.Name AS "Название группы"
FROM Departments d
JOIN Groups g ON d.Id = g.DepartmentId
ORDER BY d.Name, g.Name;


SELECT DISTINCT s.Name AS "Название дисциплины"
FROM Subjects s
JOIN Lectures l ON s.Id = l.SubjectId
WHERE l.TeacherId = 5
ORDER BY s.Name;

SELECT DISTINCT
    d.Name AS "Название кафедры"
FROM Departments d
JOIN Groups g ON d.Id = g.DepartmentId
JOIN GroupsLectures gl ON g.Id = gl.GroupId
JOIN Lectures l ON gl.LectureId = l.Id
JOIN Subjects s ON l.SubjectId = s.Id
WHERE LOWER(s.Name) = LOWER('иностранный язык')
ORDER BY d.Name;

SELECT DISTINCT g.Name AS "Название группы"
FROM Groups g
JOIN Departments d ON g.DepartmentId = d.Id
JOIN Faculties f ON d.FacultyId = f.Id
WHERE f.Name = 'Факультет точных наук'
ORDER BY g.Name;

SELECT DISTINCT
    g.Name AS "Название группы",
    f.Name AS "Название факультета"
FROM Groups g
JOIN Departments d ON g.DepartmentId = d.Id
JOIN Faculties f ON d.FacultyId = f.Id
WHERE g.Year = 2
ORDER BY f.Name, g.Name;


SELECT
    CONCAT(t.Name, ' ', t.Surname) AS "Полное имя преподавателя",
    s.Name AS "Название дисциплины",
    (SELECT g.Name FROM Groups g WHERE g.Id = gl.GroupId) AS "Название группы"
FROM Lectures l
JOIN Teachers t ON l.TeacherId = t.Id
JOIN Subjects s ON l.SubjectId = s.Id
JOIN GroupsLectures gl ON l.Id = gl.LectureId
WHERE l.LectureRoom = '205'
ORDER BY t.Surname, t.Name, s.Name;
