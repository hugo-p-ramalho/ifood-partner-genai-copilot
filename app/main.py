from fastapi import FastAPI
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
