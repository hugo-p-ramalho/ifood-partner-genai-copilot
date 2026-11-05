import os

files = {
"requirements.txt": """fastapi==0.110.0
uvicorn==0.27.1
langchain==0.2.0
langchain-openai==0.1.8
langgraph==0.1.5
langchain-community==0.2.0
python-dotenv==1.0.1
pydantic==2.7.1
chromadb==0.5.0
streamlit==1.35.0
requests==2.31.0
openai==1.30.0
""",
"data/mock_restaurantes.json": """[
  {"id": 1, "nome": "Burger King Centro", "prato": "X-Bacon", "preco": 28.90, "categoria": "lanche", "avaliacao": 4.2},
  {"id": 2, "nome": "Sushi Prime", "prato": "Hot Filadelfia", "preco": 32.00, "categoria": "japonesa", "avaliacao": 4.8}
]""",
"app/__init__.py": "",
"app/schemas.py": """from pydantic import BaseModel
from typing import List, Optional
class PratoRequest(BaseModel):
    nome_prato: str
    preco_atual: float
    categoria: str
    descricao_atual: Optional[str] = ""
class ReviewRequest(BaseModel):
    reviews: List[str]
class PratoResponse(BaseModel):
    nome_otimizado: str
    descricao_seo: str
    preco_sugerido: float
    justificativa_preco: str
    tags: List[str]
class ReviewAnalysisResponse(BaseModel):
    sentimento_geral: str
    top_reclamacoes: List[str]
    resposta_sugerida: str
    insight_acionavel: str
""",
"app/rag_store.py": """import json
def buscar_concorrentes(categoria: str):
    with open("data/mock_restaurantes.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    concorrentes = [d for d in data if d['categoria'] == categoria]
    return concorrentes if concorrentes else data[:2]
""",
"app/agents.py": """from .rag_store import buscar_concorrentes
def agente_cardapio(request):
    concorrentes = buscar_concorrentes(request.categoria)
    media_preco = sum([c['preco'] for c in concorrentes]) / len(concorrentes) if concorrentes else request.preco_atual
    preco_sugerido = round(media_preco * 0.95, 2)
    return {
        "nome_otimizado": f"{request.nome_prato} Artesanal Premium",
        "descricao_seo": f"Delicioso {request.nome_prato} feito com ingredientes selecionados.",
        "preco_sugerido": preco_sugerido,
        "justificativa_preco": f"Analisei {len(concorrentes)} concorrentes. Media R$ {media_preco:.2f}. Sugerindo R$ {preco_sugerido}",
        "tags": [request.categoria, "artesanal"]
    }
def agente_reviews(request):
    return {
        "sentimento_geral": "Misto com tendencia negativa em entrega",
        "top_reclamacoes": ["Tempo de entrega", "Embalagem amassada"],
        "resposta_sugerida": "Ola! Obrigado pelo feedback. Sentimos muito. Que tal um cupom de 15%?",
        "insight_acionavel": "32% citam ATRASO. Acao: Revisar logistica no pico 19h-21h."
    }
def orquestrador(tipo, payload):
    return agente_cardapio(payload) if tipo == "cardapio" else agente_reviews(payload)
""",
"app/main.py": """from fastapi import FastAPI
from .schemas import PratoRequest, ReviewRequest
from .agents import orquestrador
app = FastAPI(title="iFood Partner Copilot")
@app.get("/")
def health():
    return {"status": "online"}
@app.post("/gerar-cardapio")
def gerar_cardapio(req: PratoRequest):
    return orquestrador("cardapio", req)
@app.post("/analisar-reviews")
def analisar_reviews(req: ReviewRequest):
    return orquestrador("reviews", req)
""",
"frontend/app.py": """import streamlit as st, requests
st.title("iFood Partner Copilot")
nome = st.text_input("Nome do prato", "X-Burger")
preco = st.number_input("Preco", value=29.90)
cat = st.selectbox("Categoria", ["lanche", "japonesa", "italiana"])
if st.button("Gerar com IA"):
    res = requests.post("http://localhost:8000/gerar-cardapio", json={"nome_prato": nome, "preco_atual": preco, "categoria": cat}).json()
    st.success(res['nome_otimizado'])
    st.write(res['descricao_seo'])
    st.metric("Preco Sugerido", res['preco_sugerido'])
"""
}

for path, content in files.items():
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
print("✅ Projeto criado!")