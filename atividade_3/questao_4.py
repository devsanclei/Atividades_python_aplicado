# atividade 3 - questão 4

# repetir para vários alunos
while True:

    nome = input("Digite o nome do aluno: ")

    notas = []

    # receber 5 notas
    for i in range(5):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    # calcular média
    media = sum(notas) / 5

    print(f"\nAluno: {nome}")
    print(f"Média: {media}")

    # classificação
    if media >= 7:
        print("Aprovado")

    elif media >= 5:
        print("Recuperação")

    else:
        print("Reprovado")

    # continuar ou parar
    continuar = input("\nDeseja cadastrar outro aluno? (s/n): ")

    if continuar == "n":
        break