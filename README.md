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

### Atualização

PATCH /user

Já a rota patch /user pode ser usada para atualizar qualquer informação do usuário que está logado, bastando passar no corpo da requisição o dado a ser atualizado, e passar na autorização o bearer token do usuário logado, obtido no login <br>
Exemplo de requisição:

```json
{
  "email": "johndoe@email.com"
}
```

Exemplo de resposta dessa rota:

```json
{
  "name": "John Doe",
  "email": "johndoe@email.com",
  "password": "doe.john",
  "cpf": "55555555555"
}
```

### Deleção

DELETE /user <br/>

Por último, a requisição DELETE /user pode ser usada para deletar um usuário específico do banco de dados. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição, apenas uma autorização do tipo bearer token, obtida no login do usuário. <br>
A requisição bem sucedida retorna a resposta 204, sem conteúdo.

<br>

## Categoria

### Registro

POST /categories

Essa rota serve para registrar uma nova categoria no banco de dados, sendo obrigatório passar no corpo da requisição o nome da categoria a registrar. <br>
Exemplo de requisição:

```json
{
  "name": "Processadores"
}
```

Dessa requisição é esperado um retorno com os dados da categoria cadastrada, como mostrado a seguir:

```json
{
  "category_id": 1,
  "name": "Processadores"
}
```

### Listagem

GET /categories

Essa rota é usada para obter as categorias cadastradas no banco de dados. <br>
Aqui não é necessário passar nenhuma autorização, e nenhum dado no corpo da requisição.

GET /categories/\<id\>

Essa rota é usada para obter a categoria referente ao id passado na url. <br>
Aqui não é necessário passar nenhuma autorização, e nenhum dado no corpo da requisição.

### Atualização

PATCH /categories/\<id\>

Já essa rota pode ser usada para atualizar o nome da categoria referente ao id passado na url, bastando passar no corpo da requisição o dado a ser atualizado. <br>
Aqui não é necessário passar nenhuma autorização, e nenhum dado no corpo da requisição. <br>
Exemplo de requisição:

```json
{
  "name": "Armazenamentos"
}
```

Exemplo de resposta dessa rota:

```json
{
  "category_id": 1,
  "name": "Armazenamentos"
}
```

### Deleção

DELETE /categories/<\id\>

Por último, essa requisição pode ser usada para deletar uma categoria específica do banco de dados. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição, apenas a id da categoria na url da requisição. <br>
A requisição bem sucedida retorna a resposta 204, sem conteúdo.

<br>

## Produtos

### Registro

POST /products

Essa rota serve para registrar um novo produto no banco de dados, sendo obrigatório passar no corpo da requisição o model, img, price, description, e category do produto a registrar. <br>
Exemplo de requisição:

```json
{
  "model": "Processador AMD Ryzen 5 3600, AM4, 3.6GHz",
  "img": "www.img.com.br",
  "price": 1678.31,
  "description": "Marca: AMD, Modelo: Ryzen 5 3600, Cores: 6, Threads: 12, Socket: AM4, Base Clock: 3.6, Cooler Box: Incluso, GPU Integrada: Não, Consumo: 65 Watts",
  "category": "Processadores"
}
```

Dessa requisição é esperado um retorno com os dados da categoria cadastrada, como mostrado a seguir:

```json
{
  "product_id": 1,
  "model": "Processador AMD Ryzen 5 3600, AM4, 3.6GHz",
  "img": "www.img.com.br",
  "price": 1678.31,
  "description": "Marca: AMD, Modelo: Ryzen 5 3600, Cores: 6, Threads: 12, Socket: AM4, Base Clock: 3.6, Cooler Box: Incluso, GPU Integrada: Não, Consumo: 65 Watts"
}
```

### Listagem

GET /products

Essa rota é usada para obter todos os produtos cadastrados no banco de dados. <br>
Aqui não é necessário passar nenhuma autorização, e nenhum dado no corpo da requisição.

GET /products/\<id\>

Essa rota é usada para obter o produto referente ao id passado na url. <br>
Aqui não é necessário passar nenhuma autorização, e nenhum dado no corpo da requisição.

### Atualização

PATCH /products/\<id\>

Já essa rota pode ser usada para atualizar o as informações do produto referente ao id passado na url, bastando passar no corpo da requisição o dado a ser atualizado. <br>
Aqui não é necessário passar nenhuma autorização, e nenhum dado no corpo da requisição. <br>
Exemplo de requisição:

```json
{
  "model": "Processador AMD Ryzen 7 5800X, AM4, 3.8GHz",
  "description": "Marca: AMD, Modelo: Ryzen 7 5800X, Cores: 8, Threads: 16, Socket: AM4, Base Clock: 3.8, Cooler Box: Incluso, GPU Integrada: Não, Consumo: 105 Watts"
}
```

Exemplo de resposta dessa rota:

```json
{
  "product_id": 1,
  "model": "Processador AMD Ryzen 7 5800X, AM4, 3.8GHz",
  "img": "www.img.com.br",
  "price": 1678.31,
  "description": "Marca: AMD, Modelo: Ryzen 7 5800X, Cores: 8, Threads: 16, Socket: AM4, Base Clock: 3.8, Cooler Box: Incluso, GPU Integrada: Não, Consumo: 105 Watts"
}
```

### Deleção

DELETE /products/<\id\>

Por último, essa requisição pode ser usada para deletar um produto específico do banco de dados. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição, apenas a id do produto na url da requisição. <br>
A requisição bem sucedida retorna a resposta 204, sem conteúdo.

<br>

## Carrinho

### Registro

POST /cart/\<id\>

Essa rota serve para registrar um novo produto no carrinho do usuário logado. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição, apenas uma autorização do tipo bearer token, obtida no login do usuário, e a id do produto a registrar no carrinho na url da requisição. <br>
A requisição bem sucedida retorna o produto que foi adicionado ao carrinho. <br>
Exemplo de resposta da requisição:

```json
{
  "product_id": 2,
  "model": "Processador AMD Ryzen 5 3600, AM4, 3.6GHz",
  "img": "www.img.com.br",
  "price": 1678.31,
  "description": "Marca: AMD, Modelo: Ryzen 5 3600, Cores: 6, Threads: 12, Socket: AM4, Base Clock: 3.6, Cooler Box: Incluso, GPU Integrada: Não, Consumo: 65 Watts"
}
```

### Listagem

GET /cart

Essa rota é usada para obter todos os produtos adicionados no carrinho do usuário logado. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição, apenas uma autorização do tipo bearer token, obtida no login do usuário. <br>
Exemplo de resposta da requisição:

```json
{
  "total": 1678.31,
  "products": [
    {
      "model": "Processador AMD Ryzen 5 3600, AM4, 3.6GHz",
      "price": 1678.31,
      "img": "www.img.com.br",
      "description": "Marca: AMD, Modelo: Ryzen 5 3600, Cores: 6, Threads: 12, Socket: AM4, Base Clock: 3.6, Cooler Box: Incluso, GPU Integrada: Não, Consumo: 65 Watts",
      "product_id": 2
    }
  ]
}
```

### Deleção

DELETE /cart/<\id\>

Por último, essa requisição pode ser usada para deletar um produto específico do carrinho. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição, apenas uma autorização do tipo bearer token, obtida no login do usuário, e a id do produto a registrar no carrinho na url da requisição. <br>
A requisição retorna a seguinte mensagem, em caso de sucesso:

```json
{
  "msg": "Cart has been delete!"
}
```
