
# Projeto de API de Clientes - Clean Architecture

Este projeto é uma API para gerenciar clientes (criar, atualizar, visualizar e remover), seguindo os princípios da **Clean Architecture**. A aplicação foi construída usando **Flask**, **SQLAlchemy** e Docker, e inclui exemplos de rotas e configuração completa para rodar o projeto com `docker-compose`.

## Requisitos do Sistema

- **Docker** e **Docker Compose** instalados
- **Git** para clonar o repositório

### Instalação do Docker

1. **Docker**: Siga as instruções para instalar o Docker na sua máquina:
   - [Instalação do Docker](https://docs.docker.com/get-docker/)

2. **Docker Compose**: O Docker Compose geralmente é instalado junto com o Docker nas versões mais recentes.

3. **Git**: Se você ainda não tem o Git instalado, siga as instruções:
   - [Instalação do Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Como Clonar o Projeto e Rodar com Docker

1. **Clone o Repositório**

   No terminal, execute o seguinte comando para clonar o projeto:

   ```bash
   git clone https://github.com/italorudneydev/client-favorites-api
   ```

   Acesse o diretório do projeto:

   ```bash
   cd client-favorites-api
   ```

2. **Rodar o Docker Compose**

   Execute os seguintes comandos para buildar e rodar a aplicação com Docker:

   - **Buildar a imagem Docker:**

     ```bash
     docker-compose build
     ```

   - **Rodar a aplicação:**

     ```bash
     docker-compose up
     ```

   O Docker Compose irá inicializar os serviços, como o Flask, PostgreSQL e Redis.

3. **Acessar a API**

   A aplicação estará disponível em [http://localhost:5000](http://localhost:5000).

## Exemplo de Rotas

A API expõe as seguintes rotas para gerenciar clientes:

### Criar um Cliente (POST)

- **Rota**: `/clients`
- **Método**: `POST`
- **Exemplo de chamada**:

  ```bash
  curl -X POST http://localhost:5000/clients -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}'
  ```

- **Resposta** (em caso de sucesso):

  ```json
  {
    "message": "Client created success"
  }
  ```

### Atualizar um Cliente (PUT)

- **Rota**: `/clients/<client_id>`
- **Método**: `PUT`
- **Exemplo de chamada**:

  ```bash
  curl -X PUT http://localhost:5000/clients/1 -H "Content-Type: application/json" -d '{"name": "Jane Doe", "email": "jane@example.com"}'
  ```

- **Resposta** (em caso de sucesso):

  ```json
  {
    "message": "Client updated success"
  }
  ```

### Visualizar um Cliente (GET)

- **Rota**: `/clients/<client_id>`
- **Método**: `GET`
- **Exemplo de chamada**:

  ```bash
  curl http://localhost:5000/clients/1
  ```

- **Resposta** (em caso de sucesso):

  ```json
  {
    "name": "Rudney Cavalcante",
    "email": "italo@silva.com"
  }
  ```

### Remover um Cliente (DELETE)

- **Rota**: `/clients/<client_id>`
- **Método**: `DELETE`
- **Exemplo de chamada**:

  ```bash
  curl -X DELETE http://localhost:5000/clients/1
  ```

- **Resposta** (em caso de sucesso):

  ```json
  {
    "message": "Client deleted success"
  }
  ```

## Estrutura do Projeto

Aqui está uma visão geral da estrutura de diretórios do projeto, seguindo os princípios da Clean Architecture:

```
/app
│
├── /core
│   ├── /domain            # Entidades do domínio
│   ├── /use_cases         # Casos de uso
│   └── /repositories      # Interfaces de repositório
├── /adapters
│   └── /repositories      # Implementações concretas dos repositórios
├── /controllers           # Controladores para as rotas
├── /infrastructure        # Configurações e inicialização
└── /entrypoints
    └── /flask_app         # Ponto de entrada do Flask e definição de rotas
```

## Dependências do Projeto

O projeto usa as seguintes dependências, que são gerenciadas no arquivo `requirements.txt`:

- **Flask**: Framework web utilizado.
- **Flask-SQLAlchemy**: Integração do SQLAlchemy com o Flask.
- **psycopg2-binary**: Driver para PostgreSQL.
- **Flask-JWT-Extended**: Autenticação via JWT.
- **Flask-Caching**: Gerenciamento de cache com Redis.
- **python-dotenv**: Para carregar variáveis de ambiente do arquivo `.env`.

Você pode ver todas as dependências no arquivo `requirements.txt`: