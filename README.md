# LaudoPro

**LaudoPro** é uma aplicação backend para **inspeção e laudos de engenharia**, desenvolvida em **FastAPI**. Este repositório contém toda a lógica de backend da aplicação.

---

## 🔹 Funcionalidades

- Gestão de **Clientes (Customer)**
- Gestão de **Instrumentos de Medição** como **PressureGauge** e **SafetyValve**
- Gestão de **Ordens de Serviço (WorkOrder)**
- CRUD completo para todas as entidades
- Validação e serialização de dados com **Pydantic**
- Suporte a **UUID** como chave primária
- Banco de dados inicial em **SQLite**
- Estrutura organizada em camadas:  
  `models`, `schemas`, `repositories`, `services`, `routes`
- Testes automatizados com **pytest** (Service e Repository)

---

## 🔹 Estrutura do Projeto

app/
│── core/ # Configurações e dependências
│── models/ # Modelos SQLAlchemy
│── schemas/ # Pydantic Schemas
│── repositories/ # Repositórios (CRUD)
│── services/ # Lógica de negócio
│── routes/ # Rotas FastAPI
│── main.py # Entry point da aplicação
