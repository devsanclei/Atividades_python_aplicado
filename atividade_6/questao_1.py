pergunta = input("Digite sua pergunta: ").lower()

if "oi" in pergunta:
    resposta = "Olá! Como posso ajudar?"

elif "nome" in pergunta:
    resposta = "Sou um assistente virtual."

elif "python" in pergunta:
    resposta = "Python é uma linguagem de programação."

else:
    resposta = "Desculpe, não sei responder isso."

print("Resposta:", resposta)