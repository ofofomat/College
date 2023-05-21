-- How many songs each client has downloaded?

select count(cli.musicas_id) as qnt_songs, clientes.login
from musicas_has_clientes cli join clientes
on cli.clientes_id = clientes.id
group by clientes.login
order by count(cli.musicas_id) desc;