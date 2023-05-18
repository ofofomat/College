-- how many artists there are in each record company

select count(artistas.id) as qnt_artists, gravadoras.nome
from artistas left join gravadoras
on artistas.gravadoras_id = gravadoras.id
group by gravadoras.nome
order by count(artistas.id) desc;