import os

caminho = os.path.join(os.path.dirname(__file__), "dados.txt")

arquivo = open(caminho, "r", encoding="utf-8")

conteudo = arquivo.read()

arquivo.close()

print("Conteúdo do arquivo:")
print(conteudo)