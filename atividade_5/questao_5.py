import json

json_texto = '''
{
    "nome": "Sanclei t Souza",
    "idade": 24
}
'''

dados = json.loads(json_texto)

print("Nome:", dados["nome"])
print("Idade:", dados["idade"])