-- Which is the most downloaded gender from full plan's clients?

select generos.id, generos.descricao
from generos 
join musicas
on generos.id = musicas.generos_id
join musicas_has_clientes
on musicas.id = musicas_has_clientes.musicas_id
join clientes
on musicas_has_clientes.clientes_id = clientes.id
join planos
on clientes.planos_id = planos.id
group by generos.id
limit 1;