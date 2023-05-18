-- which record company has more artists

select gravadoras.nome, count(artistas.id) as qnt_artists
from gravadoras left join artistas
on gravadoras.id = artistas.gravadoras_id
group by gravadoras.nome
order by count(artistas.id) desc
limit 1;