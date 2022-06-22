# Sobre o projeto

O projeto consiste em criar algumas rotas básicas que consomem a API do Chuck Norris e retorna seus dados.

## Mapeamento das rotas

- `/api/jokes/random`
  -- Deve retornar uma única piada de forma aleatória
- `/api/jokes/category/<name>`
  -- Deve retornar uma única piada de forma aleatória para a categoria escolhida
- `/api/jokes/filter?search={query}&limit={limit}`
  -- Deve retornar uma lista de piadas de acordo com o termo pesquisado, respeitando o limite fornecido, que por padrão é 10

## Executando o projeto

A execução do projeto pode ser feita de duas formas, sendo elas: diretamente pelo console ou utilizando o Docker.

## Direto no terminal

Como pré-requisito é necessário ter o Python instalado e os pacotes Flask e requests. Para instalar os pacotes execute o comando `pip install Flask requests`.

Tendo os requisitos instalados execute o comando `python ./main.py` na raiz do projeto.

### Docker

Temos duas maneiras para executar o projeto com o Docker, utilizando o Docker Compose ou não. Abaixo temos os passos para cada uma das alternativas.

### Sem Compose

Siga os seguintes passos:

- Execute o comando `docker build -t chuck-api .` na raiz do projeto para criar a imagem
- Execute o comando `docker run --rm -d --name chuck-container -p 5000:5000 chuck-api` na raiz do projeto para inicializar o container em segundo plano
  -- Pode conferir se o container está rodando com o comando `docker ps`
  -- Caso deseje alterar a porta na sua rede altere a segundo porta no trecho do comando acima `-p 5000:[nova-porta]`

Após esses comandos o projeto estará rodando na porta 5000 da sua rede.

### Com Compose

Execute o comando `docker compose up` na raiz do projeto e seu projeto estará rodando na porta 5000 da sua rede, caso não tenha alterado no arquivo docker-compose.yml.

## Referências

- [Chuck Norris API](https://api.chucknorris.io/#!)
