# LEADS API

## URL base da API

https://pc-builder-api-v2.herokuapp.com/

## Tecnologias utilizadas

#### Framework

- Flask

#### Libraries

- Flask-SQLAlchemy <br>
- Flask-JWT-Extended <br>
- gunicorn <br>
- pdfkit <br>
- python-dotenv <br>
- Migrations <br>
- Blueprints <br>
- Dataclasses

## Inicialização da API

Para começar a utilizar a API Leads, copie a URL base da aplicação e use-a na sua ferramenta cliente de API de preferência (recomendo o Insomnia), complementando a URL com os endpoints da aplicação, explicados a seguir.

## Endpoints

<!-- Existem X endpoints nessa aplicação: X pra registro de usuário, X pra listagem dos usuários... -->

## Usuário

### Registro

POST /user/register

Essa rota serve para registrar um novo usuário no banco de dados, sendo obrigatório passar no corpo da requisição o nome, email, telefone e cpf do usuário a registrar. <br>
Exemplo de requisição:

```json
{
  "name": "John Doe",
  "email": "john@email.com",
  "password": "doe.john",
  "cpf": "55555555555"
}
```

Dessa requisição é esperado um retorno com os dados do usuário cadastrado, como mostrado a seguir:

```json
{
  "user_id": 5,
  "name": "John Doe",
  "email": "john@email.com",
  "password_hash": "pbkdf2:sha256:260000$a0LpL92dua8fES$8e027780e2970bd91a7b1dc984af8fbe87d7cc83a8701fa7699ca99a6665a1ce",
  "cpf": "55555555555",
  "addresses": [],
  "orders": []
}
```

### Login

POST /user/login

Essa rota serve para fazer login de um usuário já cadastrado no banco de dados, sendo obrigatório passar no corpo da requisição o email, e senha do usuário. <br>
Exemplo de requisição:

```json
{
  "email": "john@email.com",
  "password": "doe.john"
}
```

Dessa requisição é esperado um retorno com o token de acesso do usuário, como mostrado a seguir:

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NjQxODA3NCwianRpIjoiNWE0ZDgzODMtZThlNS00MWYzLWEwMDItN2ZlODQzOTg0YzI5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VyX2lkIjo1LCJuYW1lIjoiSm9obiBEb2UiLCJlbWFpbCI6ImpvaG5AZW1haWwuY29tIiwicGFzc3dvcmRfaGFzaCI6InBia2RmMjpzaGEyNTY6MjYwMDAwJGEwTHBMOTJkdWE4ZkVTJDhlMDI3NzgwZTI5NzBiZDkxYTdiMWRjOTg0YWY4ZmJlODdkN2NjODNhODcwMWZhNzY5OWNhOTlhNjY2NWExY2UiLCJjcGYiOiI1NTU1NTU1NTU1NSIsImFkZHJlc3NlcyI6W10sIm9yZGVycyI6W119LCJuYmYiOjE2NDY0MTgwNzQsImV4cCI6MTY0NjUwNDQ3NH0.6X5CEa9cCiauP3qjy7eKvDsVMHr2DGpkPFrRI3YFtRw"
}
```

### Listagem

GET /user

Essa rota é usada para obter os dados do usuário que está logado, cadastrado no banco de dados. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição, apenas uma autorização do tipo bearer token, obtida no login do usuário.

<!-- ### Atualização

PATCH /user

Já a rota patch /leads pode ser usada para registrar a visita de um lead, aumentando em 1 o valor da coluna "visits" do lead no banco de dados. <br>
No corpo da requisição deve ser passado apenas o email do lead a atualizar. <br>
Exemplo de requisição:

```json
{
  "email": "john@email.com"
}
```

### Deleção

DELETE /leads <br/>

Por último, a requisição DELETE /leads pode ser usada para deletar um lead específico do banco de dados, sendo necessário passar apenas o email no corpo da requisição. <br>
Exemplo de requisição:

```json
{
  "email": "john@email.com"
}
``` -->
