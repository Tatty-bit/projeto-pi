

codigo_acesso_valido = "1234"

codigo_digitado = input("Digite o código de acesso: ")

if codigo_digitado == codigo_acesso_valido:
    print("Acesso autorizado!")
else:
    print("Acesso negado. Código de acesso inválido.")