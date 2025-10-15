# 2. Escolha de arquitetura em camadas

Date: 2025-09-11

## Status
Accepted

## Context
O sistema do restaurante exige separação clara entre regras de negócio, lógica de aplicação e interface com o usuário.  
Uma arquitetura organizada facilita a manutenção, os testes e a evolução futura do projeto.

## Decision
Adotar o **estilo arquitetural em camadas (Layered Architecture)**, dividindo o sistema em:
- **Apresentação (UI)**: interface com o usuário.
- **Aplicação (Service)**: coordenação das regras de negócio.
- **Domínio (Business)**: lógica de negócio central.
- **Infraestrutura (Data, API, etc.)**: acesso a banco de dados e serviços externos.

## Consequences
Positivas:
- Maior organização e separação de responsabilidades.
- Facilidade de manutenção e testabilidade.
- Permite substituição de camadas com impacto mínimo no restante do sistema.

Negativas:
- Pode gerar sobrecarga de camadas em aplicações pequenas.
- Maior complexidade inicial de configuração.