# 4. Integração contínua com GitHub Actions

Date: 2025-09-13

## Status
Accepted

## Context
É necessário automatizar testes, builds e deploys para garantir qualidade e agilidade nas entregas.  
O projeto está hospedado no GitHub, o que permite integração direta com pipelines CI/CD.

## Decision
Adotar **GitHub Actions** como ferramenta de integração e entrega contínua.

## Consequences
Positivas:
- Integração nativa com o GitHub.
- Execução automática de testes e builds em cada push ou pull request.
- Facilita o deploy contínuo em ambientes controlados.

Negativas:
- Tempo de build pode variar conforme disponibilidade dos runners.
- Exige configuração inicial do workflow YAML.