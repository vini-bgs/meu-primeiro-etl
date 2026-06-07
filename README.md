# 🚀 meu-primeiro-etl

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-gerenciador-purple?logo=poetry&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL%20Server-local-red?logo=microsoftsqlserver&logoColor=white)
![pre-commit](https://img.shields.io/badge/pre--commit-black%20%2B%20flake8-yellow?logo=pre-commit&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)

Meu primeiro projeto de ETL (Extract, Transform, Load) desenvolvido como parte dos meus estudos em Engenharia de Dados.

O pipeline lê arquivos CSV gerados via ChatGPT simulando dados reais de uma operação de call center (avaliações de CSAT), aplica transformações e carrega os dados em um banco SQL Server local.

---

## 📋 O que o pipeline faz

1. **Extract** — lê o arquivo CSV da pasta `data/raw/`
2. **Transform** — limpa e padroniza os dados:
   - Renomeia colunas para snake_case
   - Trata valores nulos
   - Converte tipos de dados
   - Valida regras de negócio
   - Conta tickets com múltiplas avaliações
3. **Load** — carrega os dados no SQL Server em lotes de 1000 registros

---

## 🗂️ Estrutura do projeto

```
meu-primeiro-etl/
├── data/
│   └── raw/              # CSVs de entrada (não sobem para o GitHub)
├── logs/                 # Logs gerados automaticamente (não sobem para o GitHub)
├── pipeline/
│   ├── __init__.py
│   ├── extract.py        # Leitura do CSV
│   ├── transform.py      # Transformações e validações
│   ├── load.py           # Conexão e carga no SQL Server
│   └── logger.py         # Configuração centralizada de logs
├── .env                  # Variáveis de ambiente (não sobe para o GitHub)
├── .flake8               # Configuração do linter
├── .gitignore
├── .pre-commit-config.yaml
├── main.py               # Ponto de entrada do pipeline
├── poetry.lock
└── pyproject.toml
```

---

## ⚙️ Tecnologias utilizadas

| Ferramenta | Uso |
|---|---|
| Python 3.14 | Linguagem principal |
| pandas | Manipulação de dados |
| SQLAlchemy + pyodbc | Conexão com SQL Server |
| loguru | Logs do pipeline |
| python-dotenv | Variáveis de ambiente |
| Poetry | Gerenciamento de dependências |
| pre-commit | Black + flake8 antes de cada commit |

---

## 🔧 Como rodar

### Pré-requisitos

- Python 3.14+
- Poetry instalado
- SQL Server local com Windows Authentication
- ODBC Driver 17 for SQL Server

### Instalação

```bash
# Clone o repositório
git clone https://github.com/vini-bgs/meu-primeiro-etl.git
cd meu-primeiro-etl

# Instale as dependências
poetry install

# Ative o ambiente virtual
eval $(poetry env activate)
```

### Execução

```bash
poetry run python main.py
```

---

## 📁 Dados

Os dados utilizados neste projeto são fictícios, gerados via ChatGPT simulando avaliações de CSAT de uma empresa de call center. Os arquivos CSV não estão incluídos no repositório.

---

## 👨‍💻 Autor

**Vinícius** — Analista de Qualidade Jr em transição para Engenharia de Dados.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-vini--bgs-blue?logo=linkedin)](https://www.linkedin.com/in/vinícius-borges-5a7b95150)
[![GitHub](https://img.shields.io/badge/GitHub-vini--bgs-black?logo=github)](https://github.com/vini-bgs)
