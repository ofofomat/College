-- which are the songs of ACIT record company

select gravadoras.nome, musicas.nome
from musicas_has_artistas join artistas
on artistas.id = musicas_has_artistas.artistas_id join musicas 
on musicas.id = musicas_has_artistas.musicas_id join gravadoras 
on gravadoras.id = artistas.gravadoras_id
where gravadoras.nome = 'ACIT'
group by musicas.nome;