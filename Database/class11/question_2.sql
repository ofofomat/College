-- How many clients are signed up to each plan

select count(clientes.id) as client_per_plan, planos.id
from clientes left join planos
on clientes.planos_id = planos.id
group by planos.id
order by count(clientes.id) asc; 