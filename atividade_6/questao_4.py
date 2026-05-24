import json

dados = {
    "pergunta": "O que é Inteligência Artificial?"
}

json_formatado = json.dumps(
    dados,
    indent=4,
    ensure_ascii=False
)

print(json_formatado)