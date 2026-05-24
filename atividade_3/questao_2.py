# atividade 3 - questão 2 

def analisar_comentario(palavra):
    if palavra == "bom" or palavra == "ótimo" or palavra == "excelente":
        print("Comentário positivo")
    elif palavra == "ruim" or palavra == "péssimo" or palavra == "horrível":
        print("Comentário negativo")

palavra = input("Digite um comentário: ")
analisar_comentario(palavra)