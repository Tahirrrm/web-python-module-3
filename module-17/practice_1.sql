create  table departments (id SERIAL primary key,
name TEXT not null unique);

create table employees(
id SERIAL primary key, name TEXT not null, salary numeric(10,2) CHECK(salary>0),
departament_id INT references departments(id),
hired_at DATE default CURRENT_Date);

create table projects(
id Serial  primary key,
name TEXt not null, employee_id INT references employees(id),
budget Numeric(12,2) check (budget >=0),is_active BOOLEAN default true);

insert into departments(name)
values  
('it'),
('hr'),
('finance'),
('marketing');

insert into employees (name, salary, departament_id, hired_at)
valueintersect 
('Анна Иванова', 150000, 1,'2023-01-25'),
('иван петров', 90000, 1,'2023-03-10'),
('Мария смирнова', 110000, 2,'2022-11-20'),
('Олег кузнецов', 130000, 3,'2021-06-05'),
('Алексей орлов', 70000, NULL,'2024-02-01'),
('Елена соколова', 160000, 1,'2020-09-12'),
 
insert into project (name, employee_id, budget,  is_active)
values 
('CRM System',1,500000,TRUE),
('WEBSITE redesign',2,200000,TRUE),
('MIRING PLATFORM',3,300000,TRUE),
('Accounting automation',4,350000,FALSE),
('internal chat',1,150000,TRUE),
