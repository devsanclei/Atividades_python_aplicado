# atividade 3 - questão 3

# solicitar usuario e senha 
 
while True:

    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    # verificar se usuario e senha estão corretos
    if usuario == "admin" and senha == "1234":
        print("Login bem-sucedido!")
        break

    else:
     print("Usuário ou senha incorretos. Tente novamente.")