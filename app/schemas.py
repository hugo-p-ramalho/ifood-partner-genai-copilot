from pydantic import BaseModel
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
