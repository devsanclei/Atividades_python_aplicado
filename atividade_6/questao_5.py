import os

pergunta = input("Digite sua pergunta: ")

caminho = os.path.join(
    os.path.dirname(__file__),
    "historico_ia.txt"
)

arquivo = open(
    caminho,
    "a",
    encoding="utf-8"
)

arquivo.write(pergunta + "\n")

arquivo.close()

print("Pergunta salva com sucesso.")