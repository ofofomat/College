-- How many songs each gender has?

select count(musicas.id) as qnt_songs, generos.descricao
from musicas left join generos
on musicas.generos_id = generos.id
group by generos.descricao
order by count(musicas.id) desc;