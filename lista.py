

Clientes = ["Carlos","Alessandro","Elaine"]
busca = input("Dijite um nome para pesquisa:")
achou = False 
for nome in Clientes: 
    if nome.upper() == busca.upper():
        achou = True
        print("Nome encontrado na lista de clientes")
if not achou:
        print(f"Nome [{busca}] não encontrado")    
    

