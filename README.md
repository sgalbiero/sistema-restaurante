# 🍝 Sistema de Restaurante

Um sistema desenvolvido para auxiliar na gestão de restaurantes, permitindo o controle de pedidos, mesas, produtos, funcionários e pagamentos de forma simples e eficiente.

## 🚀 Tecnologias Utilizadas

- **Python 3.12+**
- **FastAPI** — Backend moderno e rápido
- **SQLite / PostgreSQL** — Banco de dados
- **SQLAlchemy** — ORM para manipulação de dados
- **Pydantic** — Validação de dados
- **Uvicorn** — Servidor ASGI para execução do projeto

## 📁 Estrutura do Projeto

sistema-restaurante/
│
├── doc/
│ └── adr/ # Arquitetura e decisões de design
│
├── src/ # Código-fonte principal
│ ├── main.py # Ponto de entrada da aplicação
│ ├── models/ # Modelos do banco de dados
│ ├── routes/ # Rotas da API
│ ├── services/ # Regras de negócio
│ └── utils/ # Funções auxiliares
│
├── tests/ # Testes automatizados
├── requirements.txt # Dependências do projeto
└── README.md # Documentação

## 🧠 ADRs (Architecture Decision Records)

As **ADRs** estão localizadas em doc/adr/ e documentam as principais decisões arquiteturais tomadas durante o desenvolvimento do sistema.

## 🤝 Contribuição

- **Faça um fork do projeto**
- **Crie uma branch: git checkout -b minha-feature**
- **Faça o commit: git commit -m 'Adiciona nova feature'**
- **Faça o push: git push origin minha-feature**
- **Abra um Pull Request 🚀**