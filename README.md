# Stylesync

é uma aplicação desenvolvida em Flask para a gestão de um sistema de inventário de produtos, utilizadores e vendas. Criado como um projeto de estudos, o foco foi a aplicação de práticas modernas de desenvolvimento back-end, validação de dados e um ambiente totalmente containerizado.

## ✨ Funcionalidades

* **Gestão de Produtos:** CRUD completo (Criar, Ler, Atualizar, Apagar) para os produtos do inventário.
* **Gestão de Usuários:** Criação, listagem e remoção de Usuários.
* **Autenticação:** Sistema de login que gera um token de acesso [JWT](https://jwt.io/) para proteger rotas sensíveis.
* **Importação em Massa:** Rota para importar vendas a partir de um ficheiro `.csv`, com validação de dados linha a linha.

## 🛠️ Tecnologias Utilizadas

A stack de desenvolvimento utilizada neste projeto inclui:

* **Framework:** [Flask](https://flask.palletsprojects.com/)
* **Banco de Dados:** [MongoDB](https://www.mongodb.com/) (NoSQL)
* **Validação de Dados:** [Pydantic](https://docs.pydantic.dev/)
* **Autenticação:** [PyJWT](https://pyjwt.readthedocs.io/)
* **Gestão de Dependências:** [Poetry](https://python-poetry.org/)
* **Containerização:** [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/)
* **Servidor WSGI:** [Gunicorn](https://gunicorn.org/)

## 🚀 Como Executar o Projeto

Para executar este projeto localmente, certifique-se de ter o **Git** e o **Docker** (com Docker Compose) instalados na sua máquina.

**1. Clonar o Repositório**
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd stylesync
```

**2. Configurar as Variáveis de Ambiente**
Crie um ficheiro chamado `.env` na raiz do projeto. Pode usar o exemplo abaixo como base.
```
# .env

# Chave secreta para o Flask (gere uma chave segura para projetos reais)
SECRET_KEY="uma-chave-secreta-forte-e-aleatoria"

# Credenciais para o banco de dados MongoDB
MONGO_USERNAME=stylesync_user
MONGO_PASSWORD=stylesync_pwd
```

**3. Construir e Iniciar os Containers**
Com o Docker em execução, execute o seguinte comando na raiz do projeto:
```bash
docker compose up --build -d
```
* O comando irá construir a imagem da sua aplicação Flask a partir do `Dockerfile`.
* Irá baixar a imagem do MongoDB.
* Irá iniciar os dois containers em segundo plano (`-d`).

**4. Aceder à Aplicação**
A API estará disponível no endereço `http://localhost:5000`.
