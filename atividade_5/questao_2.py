import requests

usuario = "devsanclei"
repositorio = "raspberry-pico-usb-numpad"

url = f"https://api.github.com/repos/{usuario}/{repositorio}"

resposta = requests.get(url)

dados = resposta.json()

print("Nome do repositório:", dados["name"])
print("Descrição:", dados["description"])
print("Linguagem principal:", dados["language"])
print("Estrelas:", dados["stargazers_count"])
print("Forks:", dados["forks_count"])
print("Criado em:", dados["created_at"])
print("Última atualização:", dados["updated_at"])
print("URL:", dados["html_url"])