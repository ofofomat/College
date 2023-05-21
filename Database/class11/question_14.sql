-- How much am I going to be paid for those who signed in my program?

select planos.descricao as name, count(clientes.planos_id) as qnt_clients, sum(planos.valor) as incoming
from planos
join clientes
on planos.id = clientes.planos_id
group by planos.descricao
order by incoming desc;
