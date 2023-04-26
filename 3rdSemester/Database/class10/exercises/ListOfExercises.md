# Exercises for Joins

## tables

```sql
CREATE TABLE cidade
(
  id integer NOT NULL,
  nome varchar2(50),
  pais varchar2(50),
  PRIMARY KEY (id)
);

CREATE TABLE pessoa
(
  id integer NOT NULL,
  nome varchar2(80),
  sobrenome varchar2(50),
  ano_nascimento integer,
  nasceu integer,
  sexo character(1),
  ano_formacao_superior integer,
  PRIMARY KEY (id),
  FOREIGN KEY (nasceu) REFERENCES cidade (id)
);

CREATE TABLE viagem
(
  id_pessoa integer NOT NULL,
  id_cidade integer NOT NULL,
  data date,
  custo decimal(6,2),
  PRIMARY KEY (id_pessoa, id_cidade),
  FOREIGN KEY (id_cidade) REFERENCES cidade (id),
  FOREIGN KEY (id_pessoa) REFERENCES pessoa (id)
);
```

## Inserts

```sql
INSERT INTO cidade VALUES (1, 'Campinas', 'Brasil');
INSERT INTO cidade VALUES (2, 'Nova York', 'Estados Unidos da América');
INSERT INTO cidade VALUES (3, 'São Paulo', 'Brasil');
INSERT INTO cidade VALUES (7, 'Berlim', 'Alemanha');
INSERT INTO cidade VALUES (5, 'Rio Branco', 'Brasil');
INSERT INTO cidade VALUES (6, 'Imperatriz', 'Brasil');
INSERT INTO cidade VALUES (8, 'Ribeirão Preto', 'Brasil');
INSERT INTO cidade VALUES (9, 'Madri', 'Espanha');
INSERT INTO cidade VALUES (4, 'Barcelona', 'Espanha');

INSERT INTO pessoa VALUES (2, 'André', 'Sousa', 1981, 1, 'M', NULL);
INSERT INTO pessoa VALUES (3, 'Pedro', 'Dias', 1935, 1, 'M', NULL);
INSERT INTO pessoa VALUES (7, 'Paulo', 'Batista', 1987, 8, 'M', NULL);
INSERT INTO pessoa VALUES (14, 'Mike', 'Von', 1971, 7, 'M', NULL);
INSERT INTO pessoa VALUES (13, 'Clarisse', 'Lopes', 1967, 8, 'F', NULL);
INSERT INTO pessoa VALUES (15, 'Franscisca', 'Sousa', 1981, 3, 'F', NULL);
INSERT INTO pessoa VALUES (17, 'Mariane', 'Ramos', 2000, 3, 'F', NULL);
INSERT INTO pessoa VALUES (20, 'Manuela', 'Andrade', 2010, 5, 'F', NULL);
INSERT INTO pessoa VALUES (21, 'Ingrid', 'Oliveira', 1960, 6, 'F', NULL);
INSERT INTO pessoa VALUES (22, 'Emanuel', 'Duarte', 1972, 8, 'M', NULL);
INSERT INTO pessoa VALUES (25, 'Simone', 'Veloso', 1952, 1, 'F', NULL);
INSERT INTO pessoa VALUES (34, 'Julio', 'Reis', 1985, 3, 'M', NULL);
INSERT INTO pessoa VALUES (1, 'Amanda', 'Silva', 1987, 1, 'F', 2013);
INSERT INTO pessoa VALUES (6, 'José', 'Antunes', 1985, 4, 'M', 2009);
INSERT INTO pessoa VALUES (10, 'Diego', 'Oliveira', 1993, 3, 'M', 2018);
INSERT INTO pessoa VALUES (11, 'Antônio', 'Silva', 1950, 4, 'M', 1975);
INSERT INTO pessoa VALUES (12, 'Josh', 'Smith', 1978, 2, 'M', 2005);
INSERT INTO pessoa VALUES (16, 'Mayara', 'Santos', 1990, 4, 'F', 2015);
INSERT INTO pessoa VALUES (50, 'Ana Paula', 'Batista', 1989, 3, 'F', 2014);
INSERT INTO pessoa VALUES (5, 'Paula', 'Andrade', 1990, 5, 'F', 2013);


INSERT INTO viagem VALUES (10, 5, to_date('2020-05-01', 'YYYY/MM/DD'), 2000);
INSERT INTO viagem VALUES (2, 7, to_date('2018-12-01', 'YYYY/MM/DD'), 5000);
INSERT INTO viagem VALUES (1, 2, to_date('2015-04-10', 'YYYY/MM/DD'), 3000);
```

## Joins

1. Listar o nome das pessoas e o nome da cidade onde nasceram;

```sql
select pessoa.nome, cidade.nome
from pessoa inner join cidade
on pessoa.nasceu = cidade.id;
```

2. Listar o nome das pessoas que viajaram, a data e o custo de cada viagem;

```sql
select pessoa.nome, viagem.data, viagem.custo
from pessoa inner join viagem
on pessoa.id = viagem.id_pessoa;
```

3. Liste o nome de odas as cidades e o nome das pessoas que ansceram nelas;

```sql
select cidade.nome, pessoa.nome
from cidade left join pessoa
on cidade.id = pessoa.nasceu
order by cidade.nome desc;
```

4. Liste todas as pessoas e o nome da cidade em que nasceram;

```sql
select pessoa.nome, cidade.nome
from cidade right join pessoa
on cidade.id = pessoa.nasceu
order by cidade.nome desc;
```

5. Liste o nome de TODAS as pessoas e o nome da cidade em que nasceram. As cidades em que ninguém nasceu também devem aparecer;

```sql
select pessoa.nome, cidade.nome
from pessoa full outer join cidade
on pessoa.nasceu = cidade.id
order by pessoa.nome asc;
```

6. Para cada cidade, recupere o nome e a quantidade de pessoas que nasceram nela;

```sql
select cidade.nome, count(pessoa.nasceu) as qnt_pessoa
from cidade left join pessoa
on cidade.id = pessoa.nasceu
group by cidade.nome
order by cidade.nome asc;
```

7. Para cada cidade em que nasceram mais de 2 pessoas, recupere o nome da cidade e a quantidade de pessoas que nasceram nela;

```sql
select cidade.nome, count(pessoa.nasceu) as qnt_pessoa
from cidade left join pessoa
on cidade.id = pessoa.nasceu
group by cidade.nome
having count(pessoa.nasceu) > 2
order by cidade.nome asc;
```
