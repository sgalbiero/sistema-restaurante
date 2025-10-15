# 3. Escolha de banco de dados PostgreSQL

Date: 2025-09-12

## Status
Accepted

## Context
O sistema precisa armazenar dados estruturados (usuários, pedidos, produtos).  
A equipe possui experiência prévia com bancos de dados relacionais, e há necessidade de garantir integridade e consistência transacional.

## Decision
Adotar **PostgreSQL** como banco de dados principal.

## Consequences
Positivas:
- Fácil integração com frameworks ORM (como SQLAlchemy ou Django ORM).
- Suporte avançado a consultas SQL, índices e extensões.
- Alta confiabilidade e aderência a padrões ACID.

Negativas:
- Maior complexidade para escalar horizontalmente.
- Configuração inicial mais detalhada em comparação com bancos NoSQL.