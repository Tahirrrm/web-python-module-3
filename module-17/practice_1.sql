create  table departments (
	id SERIAL primary key,
	name TEXT not null unique
);

create table employees(
	id SERIAL primary key, 
	name TEXT not null, 
	salary numeric(10,2) CHECK(salary>0),
	departament_id INT references departments(id),
	hired_at DATE default CURRENT_DATE
);

create table projects(
id Serial  primary key,
name TEXt not null, employee_id INT references employees(id),
budget Numeric(12,2) check (budget >=0),is_active BOOLEAN default true);

insert into departments (name)
values  
	('it'),
	('hr'),
	('finance'),
	('marketing');

insert into employees (name, salary, departament_id, hired_at)
values
	('Анна Иванова', 150000, 1,'2023-01-25'),
	('иван петров', 90000, 1,'2023-03-10'),
	('Мария смирнова', 110000, 2,'2022-11-20'),
	('Олег кузнецов', 130000, 3,'2021-06-05'),
	('Алексей орлов', 70000, NULL,'2024-02-01'),
	('Елена соколова', 160000, 1,'2020-09-12');
 
insert into projects (name, employee_id, budget,  is_active)
values 
	('CRM System',1,500000,TRUE),
	('WEBSITE redesign',2,200000,TRUE),
	('MIRING PLATFORM',3,300000,TRUE),
	('Accounting automation',4,350000,FALSE),
	('internal chat',1,150000,TRUE);


select 
name,
salary,
case 	
	when salary >= 150000 then 'high'
	when salary >= 100000 then 'middle'
	else 'low'
	end as salary_level
	from employees;

select 
	e.name as employee_name,
	coalesce(d.name,'Без отдела') as department_name
from employees e
left join departments d  on e.departament_id = d.id;


select 
	d.id,
	d.name
from departments d
where exists (
	select 1 from employees e
	where e.departament_id = d.id );

select
	e.id,
	e.name
from employees e
where exists (
	select 1 from projects p
	where p.employee_id = e.id
);
	
select 
	name as project_name,
	budget,
	case 	
		when is_active = true then 'active'
		else 'close'
	end as project_status
from projects;

	end
	
select 
	e.name as employee_name,
	count(p.id) as projects_count
from employees e
left join projects p on p.employee_id = e.id
group by e.id, e.name
order by projects_count desc;

UPDATE projects
set budget = budget + 50000
where is_active = true 
returning id,name,employee_id,budget,is_active;

DELETE FROM projects
WHERE is_active = false
returning
id,name;


