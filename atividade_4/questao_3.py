import os

nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")

caminho = os.path.join(os.path.dirname(__file__), "notas.txt")

arquivo = open(caminho, "w", encoding="utf-8")

arquivo.write(f"Nota 1: {nota1}\n")
arquivo.write(f"Nota 2: {nota2}")

arquivo.close()

print("Notas salvas com sucesso no arquivo notas.txt")