import json

pergunta = input("Digite sua pergunta: ")

dados = {
    "pergunta": pergunta,
    "resposta": "Na padaria do seu bairro vende coxinha."  # Resposta fixa para a pergunta
}

json_formatado = json.dumps(
    dados,
    indent=4,
    ensure_ascii=False
)

print(json_formatado)