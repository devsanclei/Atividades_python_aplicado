import requests
import json
import os

url = "https://restcountries.com/v3.1/name/brazil"

resposta = requests.get(url)

dados = resposta.json()

caminho = os.path.join(os.path.dirname(__file__), "dados_api.json")

arquivo = open(caminho, "w", encoding="utf-8")

json.dump(dados, arquivo, indent=4, ensure_ascii=False)

arquivo.close()

print("Dados salvos em dados_api.json")