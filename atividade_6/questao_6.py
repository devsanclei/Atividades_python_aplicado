import unicodedata

pergunta = input("Digite sua pergunta: ")

pergunta = pergunta.lower().strip()

pergunta = unicodedata.normalize(
    "NFKD",
    pergunta
).encode(
    "ASCII",
    "ignore"
).decode(
    "ASCII"
)

pergunta = pergunta.replace("?", "")
pergunta = pergunta.replace("!", "")
pergunta = pergunta.replace(".", "")

if "oi" in pergunta:

    resposta = "Olá!"

elif (
    "como voce funciona" in pergunta
    or "como vc funciona" in pergunta
):

    resposta = "Utilizo programação e IA."

else:

    resposta = "Não compreendi."

print(resposta)