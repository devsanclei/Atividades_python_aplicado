import os

resposta = input("Digite sua resposta: ")

caminho = os.path.join(os.path.dirname(__file__), "respostas.txt")

arquivo = open(caminho, "a", encoding="utf-8")

arquivo.write(resposta + "\n")

arquivo.close()

print("Resposta salva com sucesso em respostas.txt")