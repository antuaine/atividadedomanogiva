def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    Endereço = input("Digite o endereço do contato:")
    contato = nome
    print(f"Contato {nome} adicionado com sucesso!")

def buscar_contato():
    nome = input("Digite o nome do contato que deseja buscar: ")
    if nome :
        print(f"Nome: {nome}, Telefone: {[nome]}", )
    else:
        print(f"Contato {nome} não encontrado na agenda.")

# 'def listar_contatos():
#     print("Lista de contatos na agenda:")
#     for nome, telefone in contat.items():
#         print(f"Nome: {nome}, Telefone: {telefone}")'

def remover_contato():
    nome = input("Digite o nome do contato que deseja remover: ")
    if nome in :
        del [nome]
        print(f"Contato {nome} removido com sucesso!")
    else:
        print(f"Contato {nome} não encontrado na agenda.")

while True:
    print("\nOpções disponíveis:")
    print("1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Listar contatos")
    print("4. Remover contato")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1/2/3/4/5): ")
    
    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        buscar_contato()
    # elif opcao == "3":
    #     listar_contatos()
    elif opcao == "4":
        remover_contato()
    # elif opcao == "5":
    #     break
    # else:
    #     print("Opção inválida. Tente novamente.")