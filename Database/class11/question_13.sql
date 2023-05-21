-- Which are the artists and record companies with the most downloaded songs in full plans?

select artistas.nome, gravadoras.nome, count(musicas_has_clientes.musicas_id) as qnt_songs
from gravadoras
join artistas
on gravadoras.id = artistas.gravadoras_id
join musicas_has_artistas
on artistas.id = musicas_has_artistas.artistas_id
join musicas
on musicas_has_artistas.musicas_id = musicas.id
join musicas_has_clientes
on musicas.id = musicas_has_clientes.musicas_id
join clientes
on musicas_has_clientes.clientes_id = clientes.id
join planos
on clientes.planos_id = planos.id
group by artistas.nome
order by qnt_songs desc
limit 1;