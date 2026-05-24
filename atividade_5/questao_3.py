import json

dados_ia = {
    "pergunta": "O que é Python?",
    "resposta": "Python é uma linguagem de programação."
}

resultado_json = json.dumps(dados_ia, indent=4, ensure_ascii=False)

print(resultado_json)