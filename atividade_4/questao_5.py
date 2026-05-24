import os

nome = input("Digite o nome do usuário: ")

caminho = os.path.join(os.path.dirname(__file__), "acessos.txt")

arquivo = open(caminho, "a", encoding="utf-8")

arquivo.write(nome + "\n")

arquivo.close()

print("Acesso registrado com sucesso.")