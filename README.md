# 🛡️ IntelliDoc: Sistema de Revisão Técnica Pericial

O IntelliDoc é uma solução de Inteligência Artificial voltada para a perícia criminal, projetada para auxiliar na revisão de laudos e consulta a acervos técnicos. O projeto foca em privacidade e sigilo, operando de forma 100% local para garantir a integridade dos dados sensíveis.

## 🧠 Arquitetura e Conceitos Aplicados

- **Chain of Thought (CoT)**: Implementado no motor de inferência para garantir que a IA realize um raciocínio lógico passo a passo antes de emitir o parecer técnico, reduzindo alucinações em análises críticas.
- **Retrieval-Augmented Generation (RAG)**: Utilização de um banco de dados vetorial para fornecer contexto técnico à IA a partir de um acervo de laudos anteriores e manuais de procedimento (POPs). Inclui agrupamento inteligente de sentenças por contexto na indexação.
- **Validação por Pydantic**: Todas as entradas e saídas da API são rigorosamente validadas via schemas Pydantic, garantindo tipagem forte e integridade dos dados processados.
- **Observabilidade**: Logs estruturados em formato JSON (utilizando `structlog`) divididos em categorias (requisições, erros, indexador) e métricas da aplicação via Prometheus.

## 🛠️ Tecnologias e Ferramentas

- **Linguagem**: Python 3.12.
- **Framework API**: FastAPI.
- **Servidor ASGI**: Uvicorn.
- **Banco Vetorial**: ChromaDB.
- **Orquestração de LLM**: Ollama (Models: `mistral-nemo` e `nomic-embed-text`).
- **Processamento de PDF**: PyPDF2 para ingestão de documentos no RAG.
- **Observabilidade**: `structlog` (Logs) e `prometheus-fastapi-instrumentator` (Métricas).

## 🚀 Instalação e Execução

### 1. Preparação do Ambiente

```powershell
# Criação do ambiente virtual
python -m venv .venv
.\.venv\Scripts\activate

# Instalação das dependências
pip install -r requirements.txt
```

### 2. Configuração dos Modelos (Ollama)

```powershell
ollama pull mistral-nemo
ollama pull nomic-embed-text
```

### 3. Ingestão de Dados (Alimentação do RAG)

Para popular o banco vetorial com o acervo de laudos (PDFs na pasta `artifacts/Laudos_Modelo`):

```powershell
python indexar_memoria.py
```

### 4. Execução da API

```powershell
uvicorn src.api.routes:app --reload
```
Acesse o Swagger em: [http://localhost:8000/docs](http://localhost:8000/docs)  
As métricas do Prometheus estão disponíveis em: [http://localhost:8000/metrics](http://localhost:8000/metrics)

## 📡 Endpoints da API

- `POST /revisar_laudo`: Analisa a coerência técnica de um texto pericial utilizando raciocínio em cadeia (CoT).
- `POST /consultar_manual`: Busca jurisprudência e normas técnicas no acervo indexado via RAG.
- `POST /analisar_evidencia_visual`: Validação de compatibilidade entre imagens base64 e relatos periciais associados.
- `GET /metrics`: Exposição de métricas da aplicação para monitoramento e observabilidade.

## 📂 Estrutura do Projeto

```plaintext
projeto-intellidoc/
├── artifacts/           # Banco de dados vetorial e PDFs de referência
├── logs/                # Arquivos de log estruturados (requisicoes.log, erros.log, indexador.log)
├── src/
│   ├── api/            # Rotas e lógica FastAPI
│   ├── models/         # Schemas de validação Pydantic
│   ├── services/       # Integração com Ollama e lógica de negócio
│   └── utils/          # Utilitários, como configuração do logger estruturado
├── indexar_memoria.py   # Script de ingestão do RAG
└── teste_api.py        # Script utilitário/entrypoint
```

---

**Autor**: Everaldo – Aluno do MBA EM INTELIGÊNCIA ARTIFICIAL GENERATIVA - PCDF.