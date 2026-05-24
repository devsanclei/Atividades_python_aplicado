import os

mensagem = input("Digite uma mensagem: ")

caminho = os.path.join(os.path.dirname(__file__), "chatbot.txt")

arquivo = open(caminho, "w", encoding="utf-8")

arquivo.write(mensagem)

arquivo.close()

print("Mensagem salva com sucesso no arquivo chatbot.txt")