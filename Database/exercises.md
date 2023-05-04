# Exercícios de reforço

1. Selecione todos os ids, nomes e sobrenomes de empregados que estejam na faixa de salários de 0 a 2000 reais e maiores ou iguais a 5000 reais.

```sql
select employee_id, first_name, last_name
from hr.employees
where salary >= 0 and salary <= 2000 or salary >=5000;
-- where option two
-- where salary between 0 and 2000 or salary >=5000
-- where option three
-- where salary not between 2001 and 4999
```

2. Selecione todos os ids e nome de departamentos, o id do gerente do departamento que estejam no ide de locais entre 1500 e 2000.

```sql
select department_id, department_name, manager_id
from hr.departments
where location_id between 1500 and 2000;
```

3. Selecione todos os nomes de departamentos e nomes dos gerentes de departamentos onde a cidade de localização seja SP

```sql
select department_name, first_name
from hr.departments right join ht.employees
on hr.departments.manager_id = hr.employees.manager_id inner join hr.locations
on hr.departments.location_id = hr.locations.location_id
where city = 'Sao Paulo';
```

option 2

```sql
select department_name, first_name
from hr.departments, hr.employees, hr.locations
where hr.departments.manager_id = hr.employees.manager_id
and hr.departments.location_id = hr.locations.location_id
and city = 'Sao Paulo';
```

4. Selecione todos os ids, nomes e sobrenomes de empregados que possuem salário maior que 5000

```sql
select employee_id, first_name, last_name
from hr.employees
where salary > 5000;
-- option two
select employee_id, first_name, last_name
from hr.employees
where salary not between 0 and 5000;
```

5. Selecione todos os ids, nomes e sobrenomes (como campo único - nome completo) dos empregados, a data de admissão (hire_date), data de início e fim dos serviços (jobs)

```sql
select (concat(concat(concat(employees.employee_id, ': ')first_name, ' ')last_name)) as full_name, hire_date, start_date, end_date
from hr.employees inner join hr.job_history
on hr.job_history.employee_id = hr.employees.employee_id;
```

6. Selecione o nome da região, o nome dos países que iniciem com as letras A, B e J.

```sql
select hr.regions.region_name, hr.countries.country_name
from hr.regions inner join hr.countries
on hr.countries.region_id = hr.regions_region_id
where country_name like 'A%' or country_name like 'B%' or country_name like 'J%';
-- option two
select hr.regions.region_name, hr.countries.country_name
from hr.regions, hr.countries
where hr.countries.region_id = hr.regions.region_id
and country_name like 'A%' or country_name like 'B%' or country_name like 'J%';
```
