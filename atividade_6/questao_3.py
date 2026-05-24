import requests

traducao = {
    "ação": "Action",
    "comédia": "Comedy",
    "terror": "Horror"
}

url = "https://api.tvmaze.com/shows"

resposta = requests.get(url)

dados = resposta.json()

while True:

    genero = input(
        "\nDigite o gênero (ação, comédia, terror) ou 'sair': "
    ).lower()

    if genero == "sair":

        print("Programa encerrado.")

        break

    filme = "Nenhuma recomendação encontrada."

    if genero in traducao:

        genero_api = traducao[genero]

        for serie in dados:

            if genero_api in serie["genres"]:

                filme = serie["name"]

                break

    else:

        filme = "Gênero inválido."

    print("Recomendação:", filme)