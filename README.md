# <b> LEADS API </b>

## <b> URL base da API </b>

https://pc-builder-api-v2.herokuapp.com/

## <b> Tecnologias utilizadas </b>

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

<br>

## <b> > Inicialização da API </b>

Para começar a utilizar a API Leads, copie a URL base da aplicação e use-a na sua ferramenta cliente de API de preferência (recomendo o Insomnia), complementando a URL com os endpoints da aplicação, explicados a seguir.

<br>

<br>

## <b> > Endpoints </b>

<!-- Existem X endpoints nessa aplicação: X pra registro de usuário, X pra listagem dos usuários... -->

<br>

<br>

## <b> > Usuário </b>

<br>

### <b> Registro </b>

<i> POST /user/register </i>

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
  "user_id": 1,
  "name": "John Doe",
  "email": "john@email.com",
  "cpf": "55555555555",
  "addresses": [],
  "orders": [],
  "cart": {
    "total": 0.0,
    "products": []
  }
}
```

<br>

### <b> Login </b>

<i> POST /user/login </i>

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

<br>

### <b> Listagem </b>

<i> GET /user </i>

Essa rota é usada para obter os dados do usuário que está logado, cadastrado no banco de dados. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição, apenas uma autorização do tipo bearer token, obtida no login do usuário. <br>
Exemplo de resposta dessa rota:

```json
{
  "user_id": 1,
  "name": "John Doe",
  "email": "john@email.com",
  "cpf": "55555555555",
  "addresses": [],
  "orders": []
}
```

<br>

### <b> Atualização </b>

<i> PATCH /user </i>

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

<br>

### <b> Deleção </b>

<i> DELETE /user </i>

Por último, a requisição DELETE /user pode ser usada para deletar um usuário específico do banco de dados. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição, apenas uma autorização do tipo bearer token, obtida no login do usuário. <br>
A requisição bem sucedida retorna a resposta 204, sem conteúdo.

<br>

<br>

## <b> > Categoria </b>

<br>

### <b> Registro </b>

<i> POST /categories </i>

Essa rota serve para registrar uma nova categoria no banco de dados, sendo obrigatório passar no corpo da requisição o nome da categoria a registrar. <br>
Essa rota é protegida pela autorização bearer token de administrador. <br>
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

<br>

### <b> Listagem </b>

<br>

<i> GET /categories </i>

Essa rota é usada para obter as categorias cadastradas no banco de dados. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição. <br>
Essa rota é protegida pela autorização bearer token de administrador. <br>
Exemplo de resposta dessa requisição:

```json
[
  {
    "category_id": 1,
    "name": "Processadores"
  },
  {
    "category_id": 2,
    "name": "Periféricos"
  }
]
```

<i> GET /categories/\<id\> </i>

Essa rota é usada para obter a categoria referente ao id passado na url. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição. <br>
Essa rota é protegida pela autorização bearer token de administrador. <br>
Exemplo de resposta dessa requisição:

```json
{
  "category_id": 1,
  "name": "Processadores"
}
```

<br>

### <b> Atualização </b>

<i> PATCH /categories/\<id\> </i>

Já essa rota pode ser usada para atualizar o nome da categoria referente ao id passado na url, bastando passar no corpo da requisição o dado a ser atualizado. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição. <br>
Essa rota é protegida pela autorização bearer token de administrador. <br>
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

<br>

### <b> Deleção </b>

<i> DELETE /categories/<\id\> </i>

Por último, essa requisição pode ser usada para deletar uma categoria específica do banco de dados. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição, apenas a id da categoria na url da requisição. <br>
Essa rota é protegida pela autorização bearer token de administrador. <br>
A requisição bem sucedida retorna a resposta 204, sem conteúdo.

<br>

<br>

## <b> > Produtos </b>

<br>

### <b> Registro </b>

<i> POST /products </i>

Essa rota serve para registrar um novo produto no banco de dados, sendo obrigatório passar no corpo da requisição o model, img, price, description, e category do produto a registrar. <br>
Essa rota é protegida pela autorização bearer token de administrador. <br>
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

Dessa requisição é esperado um retorno com os dados do produto cadastrado, como mostrado a seguir:

```json
{
  "product_id": 1,
  "model": "Processador AMD Ryzen 5 3600, AM4, 3.6GHz",
  "img": "www.img.com.br",
  "price": 1678.31,
  "description": "Marca: AMD, Modelo: Ryzen 5 3600, Cores: 6, Threads: 12, Socket: AM4, Base Clock: 3.6, Cooler Box: Incluso, GPU Integrada: Não, Consumo: 65 Watts"
}
```

<br>

### <b> Listagem </b>

<i> GET /products </i>

Essa rota é usada para obter todos os produtos cadastrados no banco de dados. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição. <br>
Essa rota é protegida pela autorização bearer token de administrador. <br>
Exemplo de resposta dessa requisição:

```json
[
  {
    "product_id": 1,
    "model": "Processador AMD Ryzen 5 3600, AM4, 3.6GHz",
    "img": "www.img.com.br",
    "price": 1678.31,
    "description": "Marca: AMD, Modelo: Ryzen 5 3600, Cores: 6, Threads: 12, Socket: AM4, Base Clock: 3.6, Cooler Box: Incluso, GPU Integrada: Não, Consumo: 65 Watts"
  }
]
```

<i> GET /products/\<id\> </i>

Essa rota é usada para obter o produto referente ao id passado na url. <br>
Aqui não é necessário passar nenhuma autorização, e nenhum dado no corpo da requisição.<br>
Essa rota é protegida pela autorização bearer token de administrador. <br>
Exemplo de resposta dessa requisição:

```json
{
  "product_id": 1,
  "model": "Processador AMD Ryzen 5 3600, AM4, 3.6GHz",
  "img": "www.img.com.br",
  "price": 1678.31,
  "description": "Marca: AMD, Modelo: Ryzen 5 3600, Cores: 6, Threads: 12, Socket: AM4, Base Clock: 3.6, Cooler Box: Incluso, GPU Integrada: Não, Consumo: 65 Watts"
}
```

<br>

### <b> Atualização </b>

<i> PATCH /products/\<id\> </i>

Já essa rota pode ser usada para atualizar as informações do produto referente ao id passado na url, bastando passar no corpo da requisição o dado a ser atualizado. <br>
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

<br>

### <b> Deleção </b>

<i> DELETE /products/<\id\> </i>

Por último, essa requisição pode ser usada para deletar um produto específico do banco de dados. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição, apenas a id do produto na url da requisição. <br>
A requisição bem sucedida retorna a resposta 204, sem conteúdo.

<br>

<br>

## <b> > Carrinho </b>

<br>

### <b> Registro </b>

<i> POST /cart/\<id\> </i>

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

<br>

### <b> Listagem </b>

<i> GET /cart </i>

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

<br>

### <b> Deleção </b>

<i> DELETE /cart/<\id\> </i>

Por último, essa requisição pode ser usada para deletar um produto específico do carrinho. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição, apenas uma autorização do tipo bearer token, obtida no login do usuário, e a id do produto a registrar no carrinho na url da requisição. <br>
A requisição retorna a seguinte mensagem, em caso de sucesso:

```json
{
  "msg": "Cart has been delete!"
}
```

<br>

<br>

## <b> > Endereços </b>

<br>

### <b> Registro </b>

<i> POST /address </i>

Essa rota serve para registrar um novo endereço ao usuário logado, sendo obrigatório passar no corpo da requisição o cep, cidade, estado, logradouro, e numero do endereço a registrar, além de uma autorização do tipo bearer token, obtida no login do usuário. <br>
Exemplo de requisição:

```json
{
  "cep": "20221410",
  "cidade": "Rio de Janeiro",
  "estado": "RJ",
  "logradouro": "Rua Alexandre Mackenzie",
  "numero": 15
}
```

Dessa requisição é esperado um retorno com os dados do endereço cadastrado, como mostrado a seguir:

```json
{
  "zip_code": "20221410",
  "state": "RJ",
  "city": "Rio de Janeiro",
  "public_place": "Rua Alexandre Mackenzie",
  "number": 15
}
```

<br>

### <b> Listagem </b>

<i> GET /address </i>

Essa rota é usada para obter todos os endereços cadastrados para o usuário logado. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição, apenas uma autorização do tipo bearer token, obtida no login do usuário. <br>
Exemplo de resposta dessa requisição:

```json
[
  {
    "address_id": 9,
    "zip_code": "20221410",
    "state": "RJ",
    "city": "Rio de Janeiro",
    "public_place": "Rua Alexandre Mackenzie",
    "number": 15
  }
]
```

<br>

### <b> Atualização </b>

<i> PUT /address/\<id\> </i>

Já essa rota pode ser usada para atualizar as informações do endereço referente ao id passado na url, bastando passar no corpo da requisição o endereço inteiro a ser atualizado, com os campos obrigatórios zip_code, state, city, public_place e number. <br>
Aqui também é necessário passar uma autorização do tipo bearer token, obtida no login do usuário. <br>
Essa rota devolve a resposta 204 - sem conteúdo. <br>
Exemplo de requisição:

```json
{
  "zip_code": "20221410",
  "state": "RJ",
  "city": "Rio de Janeiro",
  "public_place": "Rua Vinicius de Morais",
  "number": 25
}
```

<br>

### <b> Deleção </b>

<i> DELETE /address/<\id\> </i>

Por último, essa requisição pode ser usada para deletar um endereço específico cadastrado para o usuário logado. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição, apenas a id do produto na url da requisição e uma autorização do tipo bearer token, obtida no login do usuário. <br>
A requisição bem sucedida retorna a resposta 204 - sem conteúdo.

<br>

<br>

## <b> > Pedidos </b>

### <b> Listagem </b>

<i> GET /orders </i>

Essa rota é usada para obter todos os pedidos do usuário logado. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição, apenas uma autorização do tipo bearer token, obtida no login do usuário. <br>
Exemplo de resposta dessa requisição:

<!-- ```json
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
``` -->

<i> GET /orders/\<id\> </i>

Essa rota é usada para obter o pedido do usuário logado, referente ao id passado na url. <br>
Aqui não é necessário passar nenhum dado no corpo da requisição, apenas a id do produto na url da requisição e uma autorização do tipo bearer token, obtida no login do usuário.<br>
Exemplo de resposta dessa requisição:

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
