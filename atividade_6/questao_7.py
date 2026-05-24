while True:

    pergunta = input(
        "Digite sua pergunta (ou 'sair'): "
    ).lower().strip()

    if pergunta == "sair":

        print("Programa encerrado.")

        break

    elif "oi" in pergunta:

        print("Olá!")

    elif (
        "como voce funciona" in pergunta
        or "como vc funciona" in pergunta
    ):

        print("Utilizo programação e IA.")

    elif (
        "qual seu nome" in pergunta
    ):

        print("Sou um chatbot simples.")

    elif (
        "que horas sao" in pergunta
    ):

        print("Não tenho acesso ao horário atual.")

    else:

        print("Não compreendi.")