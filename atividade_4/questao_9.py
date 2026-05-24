import os

genero = input("Digite seu gênero favorito (ação, comédia, terror): ").strip().lower()

if genero == "ação":
    recomendacao = "John Wick"

elif genero == "comédia":
    recomendacao = "As Branquelas"

elif genero == "terror":
    recomendacao = "Invocação do Mal"

else:
    recomendacao = "Gênero não encontrado."

caminho = os.path.join(os.path.dirname(__file__), "recomendacoes.txt")

arquivo = open(caminho, "w", encoding="utf-8")

arquivo.write(f"Gênero favorito: {genero}\n")
arquivo.write(f"Recomendação: {recomendacao}")

arquivo.close()

print("Recomendação salva com sucesso em recomendacoes.txt")