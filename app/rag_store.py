import json
def buscar_concorrentes(categoria: str):
    with open("data/mock_restaurantes.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    concorrentes = [d for d in data if d['categoria'] == categoria]
    return concorrentes if concorrentes else data[:2]
