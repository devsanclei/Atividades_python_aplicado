import os

nome = input("Digite o nome do usuário: ")

caminho = os.path.join(os.path.dirname(__file__), "usuarios.txt")

arquivo = open(caminho, "w", encoding="utf-8")

arquivo.write(nome)

arquivo.close()

print("Nome salvo com sucesso.")