import os

caminho = os.path.join(os.path.dirname(__file__), "tarefas.txt")

arquivo = open(caminho, "w", encoding="utf-8")

for i in range(3):
    tarefa = input(f"Digite a tarefa {i + 1}: ")
    arquivo.write(tarefa + "\n")

arquivo.close()

print("Tarefas salvas com sucesso em tarefas.txt")