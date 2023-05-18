-- which are the songs from Mano Lima

select musicas.id, musicas.nome
from musicas inner join musicas_has_artistas
on musicas.id = musicas_has_artistas.musicas_id
where musicas_has_artistas.artistas_id = 1
order by musicas.id asc;