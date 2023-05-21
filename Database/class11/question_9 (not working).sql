-- what are - if there's any - the songs that were never downloaded? (artist name and music name)

select artistas.nome as artistas, musicas.nome as musicas
from musicas 
join musicas_has_clientes
on musicas_has_clientes.musicas_id = musicas.id 
join musicas_has_artistas
on musicas.id = musicas_has_artistas.musicas_id 
join artistas
on musicas_has_artistas.artistas_id = artistas.id
where musicas.id not in (
	select musicas_has_clientes.musicas_id
    from musicas_has_clientes
)
group by artistas.nome
order by artistas.nome asc;