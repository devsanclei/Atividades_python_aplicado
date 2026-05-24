# Lista de palavras positivas
palavras_positivas = [
    "amor", "alegria", "felicidade", "esperança",
    "amizade", "sucesso", "paz", "gratidão",
    "confiança", "otimismo"
]

contador = 0

while True:
    palavra = input("Digite uma palavra (ou 'sair' para encerrar): ").strip().lower()

    if palavra == "sair":
        break

    if palavra in palavras_positivas:
        contador += 1

print(f"O número de palavras positivas digitadas é: {contador}")