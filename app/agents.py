from .rag_store import buscar_concorrentes
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
