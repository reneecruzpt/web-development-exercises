# Curso Prático de Desenvolvimento Web — HTML, CSS, Flask & SQLite

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-black?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Repositório curricular contendo uma **jornada progressiva e prática de desenvolvimento web full-stack**, desde os fundamentos de estruturação semântica com HTML5 e estilização com CSS3 até à construção de servidores web dinâmicos em **Python / Flask** com persistência em base de dados relacional **SQLite**.

---

## 📚 Índice Curricular e Módulos

### 🧱 [AULA 1 — Fundamentos de HTML5 e Estrutura Semântica](AULA%201)
- **Task 1:** Tags essenciais de marcação e hierarquia de títulos (`h1`-`h6`, `p`).
- **Task 2:** Referências, hiperligações externas e incorporação de ilustrações.
- **Task 3:** Formatação de texto e poemas com quebras de linha controladas.
- **Task 4:** Listas ordenadas (`<ol>`) e não ordenadas (`<ul>`).
- **Task 5:** Construção de uma página web temática de jogos (*Gamer's Web Page*).
- **Desafios Bónus:** Páginas de estações do ano, lista de tarefas (*To-Do List*) e biografia.

### 🎨 [AULA 2 — Estilização, Cores e Layout com CSS3](AULA%202)
- **Task 1:** Paleta e aplicação de cores em texto e fundos.
- **Task 2:** Estilos avançados de fundo e propriedades de contorno.
- **Task 3 & 4:** Formatação de blocos de código com destaque visual e listas de fatos.
- **Task 5:** Estruturação de texto e artigos em múltiplas colunas responsivas.

### 💾 [AULA 3 — Introdução a Bases de Dados Relacionais & SQLite](AULA%203)
- **Task 1:** Consultas SQL fundamentais (`SELECT`, `WHERE`, `ORDER BY`).
- **Task 2:** Primeira integração entre o motor **SQLite3** e rotas web em **Flask**.

### 🗄️ [AULA 4 — Modelação Relacional e Arquitetura de Quiz](AULA%204)
- **Task 1:** Modelação de tabelas relacionais com chaves primárias e estrangeiras.
- **Task 2:** Povoamento automatizado de tabelas com dados de perguntas e alternativas.
- **Task 3:** Consultas dinâmicas de recuperação de perguntas para o motor do jogo.
- **db_scripts.py:** Módulo de abstração de acesso a dados (*Data Access Layer*).

### 🌐 [AULA 5 — Rotas Dinâmicas, Sessões HTTP e Interface Web](AULA%205)
- **Regras de URL:** Parâmetros de rota dinâmicos no Flask.
- **Gestão de Sessões (`Flask.session`):** Manutenção do estado do utilizador e pontuação ao longo das rondas.
- **Quiz_Interface:** Templates HTML (`first.html`) e folhas de estilo CSS (`style.css`) integradas.
- **Contador:** Tarefas bónus de manipulação de contadores por sessão.

### 📝 [AULA 6 — Formulários HTML e Receção de Dados](AULA%206)
- **Formulários Interativos:** Questionários, telas de autenticação/login e formulários de reserva.
- **Processamento de Requisições:** Captura e validação de métodos `POST`/`GET` em Python.
- **Ciclo Completo:** Envio de formulário -> Validação no backend -> Gravação em base de dados -> Resposta dinâmica.

---

## 🚀 Como Executar os Exercícios de Flask

### 1. Clonar o Repositório
```bash
git clone https://github.com/reneecruzpt/web-development-exercises.git
cd web-development-exercises
```

### 2. Criar e Ativar Ambiente Virtual
```bash
python -m venv .venv
# No Windows:
.venv\Scripts\activate
# No Linux/macOS:
source .venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Executar uma Aplicação (exemplo Aula 5 - Quiz com Sessão):
```bash
cd "AULA 5/2 - VSC. Sessions"
python quiz.py
```
Aceda ao servidor no seu navegador em `http://127.0.0.1:5000`.

---

## 📄 Licença
Distribuído sob a licença MIT.
