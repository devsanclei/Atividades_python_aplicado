# atividade 3 - questão 5

#loop para interação continua 
while True:
    mensagem = input("Você: ")
    if mensagem == "oi":
        print("Chatbot: Olá! Como posso ajudar você hoje?")

    elif mensagem == "tchau":
        print("Chatbot: Tchau! Tenha um ótimo dia!")
        break
    else:
        print("Chatbot: Desculpe, não entendi. Por favor, tente novamente.")