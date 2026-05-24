import requests

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

resposta = requests.get(url)

dados = resposta.json()

cotacao = dados["USDBRL"]["bid"]

print(f"Cotação atual do dólar: R$ {cotacao}")