palavra = input("Digite uma palavra: ").lower()

if palavra in ["bom", "ótimo", "feliz", "alegria"]:
    sentimento = "Positivo"

elif palavra in ["ruim", "péssimo", "triste", "raiva"]:
    sentimento = "Negativo"

else:
    sentimento = "Neutro"

print("Sentimento:", sentimento)