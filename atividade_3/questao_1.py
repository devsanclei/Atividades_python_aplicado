# atividade 3
# Questão 1

# definindo elementos da construção do codigo
# pedir o genero do filme
# verificar se é ação
# verificar se é comedia
# verificar se é terror

# caso seja outro valor

genero = input("Digite um gênero: ")

if genero == "ação":
    # mostrar recomendação
    print("John Wick 4")

elif genero == "comédia":
    # mostrar recomendação
    print("Se Beber Não Case")

elif genero == "terror":
    # mostrar recomendação
    print("A Freira")

else:
    print("gênero inválido, digite corretamente")