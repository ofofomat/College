-- which are the plans and its values and download limit

select planos.id, planos.descricao, planos.valor, planos.limite
from planos
order by planos.id asc;