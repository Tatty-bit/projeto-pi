
clientes = []
def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    idade = input("Digite a idade do cliente: ")
    email = input("Digite o e-mail do cliente: ")
    
    cliente = {
        "nome": nome,
        "idade": idade,
        "email": email
    }
    
    clientes.append(cliente)
    print("✅ Cliente cadastrado com sucesso!\n")

cadastrar_cliente()


print("📋 Clientes cadastrados:")
print(clientes)