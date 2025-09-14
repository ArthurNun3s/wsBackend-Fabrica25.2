# Desafio Back-end 25.2 - Gerenciador de Torneios

Aplicação web com Django para gerenciar torneios e jogadores de jogos de luta. O projeto implementa funcionalidades de CRUD para as entidades e consome a API externa da RAWG para exibir dados de jogos.

## 🚀 Funcionalidades

* CRUD completo para Jogadores e Torneios.
* Relacionamento Many-to-Many entre Torneios e Jogadores.
* Consumo da API da RAWG para exibir os jogos mais bem avaliados na página inicial.
* Interface renderizada com o sistema de Templates do Django.

## 🛠️ Tecnologias Utilizadas

* Python / Django
* Requests
* Python Decouple
* HTML / CSS (Bootstrap)

## ⚙️ Setup e Execução

1.  Clone o repositório.
2.  Navegue até a pasta do projeto e crie/ative um ambiente virtual (`venv`).
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4.  Crie o arquivo `.env` na raiz do projeto, utilizando o `.env.example` como base, e adicione sua chave da API RAWG.
5.  Aplique as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```
6.  Crie um superusuário para acessar o painel de admin:
    ```bash
    python manage.py createsuperuser
    ```
7.  Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
    * O site estará disponível em `http://127.0.0.1:8000/`.
    * O painel de admin estará em `http://127.0.0.1:8000/admin/`.

## ✒️ Autor

* Arthur Nunes Campos Rodrigues