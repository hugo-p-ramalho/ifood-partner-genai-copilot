# 🍔 iFood Partner Copilot - GenAI Agent

> Projeto desenvolvido para o processo seletivo **iFood - Programa GenAI 2027 | Trilha AI Builder**

Um copiloto de IA que ajuda restaurantes parceiros do iFood a venderem mais, com otimização de cardápio e análise de reviews usando agentes de IA e RAG.

### 🎯 Problema real do iFood
Restaurantes parceiros perdem conversão por descrições ruins e precificação fora do mercado. A solução é um AI Builder B2B que gera receita para o parceiro.

### 🏗️ Arquitetura Escalável

[ Streamlit Frontend ] -> [ FastAPI API Stateless ] -> [ Orchestrator Agent ]
                                                     -> [ Agent Cardápio + Agent Reviews ]
                                                     -> [ RAG Store (Chroma / pgvector) ]

**Decisões de escalabilidade:**
- API desacoplada do frontend, pronta para Kubernetes
- RAG desacoplado (troca de Chroma para pgvector com 1 linha)
- Tracing pronto para LangSmith / Langfuse
- Modo MOCK para rodar sem chave, modo PROD com OpenAI

### 🚀 Como rodar

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# em outro terminal
streamlit run frontend/app.py

- API Docs: http://localhost:8000/docs
- App: http://localhost:8501

### 🔮 Roadmap
- Migrar para LangGraph StateGraph real
- Trocar para pgvector em produção
- Adicionar LangSmith tracing e avaliação
- Guardrails para precificação

Feito por Hugo P. Ramalho para a vaga de AI Builder do iFood.
