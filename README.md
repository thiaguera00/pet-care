# 🐾 Pet Care - Sistema de Gerenciamento de Pets e Clínicas
Este projeto foi desenvolvido na disciplina Aplicações para internet, ministrada pelo professor Mauro.
É uma aplicação fullstack para gerenciamento de pets e clínicas veterinárias. Ele é dividido em dois principais componentes:

- **📦 Backend (API)**: Desenvolvido com **FastAPI**, responsável por toda a lógica de negócios e armazenamento.
- **🎨 Frontend (Admin)**: Desenvolvido com **Django**, responsável pela interface administrativa e dashboards com gráficos.

---

## 🚀 Tecnologias Utilizadas

### Backend (FastAPI)

- FastAPI
- SQLAlchemy (ORM)
- SQLite
- JWT Authentication (via `passlib`, `python-jose`)
- Uvicorn / uv (servidor)
- Estrutura com separação de camadas:
  - `router/`, `service/`, `repository/`, `database/`, `dtos/`

### Frontend (Django)

- Django (views, templates)
- Requests (para consumir API FastAPI)
- Plotly (para gráficos interativos no dashboard)
- Bootstrap e HTML5/CSS3 para estilização

---
Desenvolvido por: Júlia Souza, Larissa Novaes e Thiago Caetano
