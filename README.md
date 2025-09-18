# Desafio Back-end 25.2 - Gerenciador de Torneios

Este projeto é uma aplicação web desenvolvida com Django que serve como um gerenciador de torneios de jogos de luta. Ele permite a criação, visualização, atualização e deleção (CRUD) de jogadores e torneios, e também consome uma API externa para exibir informações sobre jogos populares.

## 🚀 Funcionalidades

* **CRUD completo de Jogadores:** Adicione, liste, edite e apague jogadores, especificando seus personagens.
* **CRUD completo de Torneios:** Crie, liste, edite e apague torneios.
* **Relacionamento de Entidades:** Inscreva jogadores em torneios através do painel de administração do Django.
* **Consumo de API Externa:** A página inicial exibe os jogos mais bem avaliados do momento, consumindo dados em tempo real da [RAWG Video Games Database API](https://rawg.io/apidocs).
* **Interface com Templates:** O projeto utiliza o sistema de templates do Django para renderizar páginas HTML funcionais e organizadas.

## 🛠️ Tecnologias Utilizadas

* Python
* Django
* Requests (para consumo de API)
* Python Decouple (para gerenciamento de variáveis de ambiente)
* HTML / CSS (Bootstrap básico para estilização)

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para executar o projeto localmente.

### 1. Pré-requisitos
- Python 3.8 ou superior
- Git

### 2. Clonar o Repositório
```bash
git clone [https://github.com/](https://github.com/)[SEU_USUARIO_GITHUB]/wsBackend-Fabrica25.2.git
cd wsBackend-Fabrica25.2
```

### 3. Criar e Ativar o Ambiente Virtual
```bash
# Criar o venv
python -m venv venv

# Ativar no Windows
.\venv\Scripts\activate

# Ativar no macOS/Linux
source venv/bin/activate
```

### 4. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 5. Configurar as Variáveis de Ambiente (MUITO IMPORTANTE)
Este projeto precisa de uma chave de API para funcionar.

-   Na raiz do projeto, crie um arquivo chamado `.env`.
-   Dentro do `.env`, adicione a seguinte linha, substituindo `SUA_CHAVE_AQUI` pela sua chave da API RAWG:
    ```
    RAWG_API_KEY=SUA_CHAVE_AQUI
    ```

### 6. Aplicar as Migrações do Banco de Dados
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Criar um Superusuário (para acesso ao Admin)
```bash
python manage.py createsuperuser
```
Siga os passos para criar seu usuário e senha.

### 8. Rodar o Servidor
```bash
python manage.py runserver
```
O site estará disponível em `http://127.0.0.1:8000/`.

## 🌐 Estrutura do Site

-   `/`: Página inicial com a lista de jogos da API externa.
-   `/players/`: Lista todos os jogadores, com opções de Editar e Apagar.
-   `/players/new/`: Formulário para criar um novo jogador.
-   `/tournaments/`: Lista todos os torneios.
-   `/admin/`: Painel de administração do Django para gerenciar as relações entre jogadores e torneios.

## ✒️ Autor

-   **[SEU NOME AQUI]**
