import os

palavras_positivas = ["bom", "ótimo"]
palavras_negativas = ["ruim", "péssimo"]

palavra = input("Digite uma palavra: ").strip().lower()

if palavra in palavras_positivas:
    resultado = "Positivo"

elif palavra in palavras_negativas:
    resultado = "Negativo"

else:
    resultado = "Sentimento não identificado"

caminho = os.path.join(os.path.dirname(__file__), "sentimentos.txt")

arquivo = open(caminho, "w", encoding="utf-8")

arquivo.write(f"Palavra digitada: {palavra}\n")
arquivo.write(f"Resultado da análise: {resultado}")

arquivo.close()

print("Análise salva com sucesso em sentimentos.txt")