dadosDoEstoque = [
    [0, "Martelo", 23, 34],
    [1, "Rosca", 21, 89],
    [2, "Engrenagem", 34, 4]
] ## ID, Nome, quantidade, localização
novoID = 2

print("------------------SEJA BEM-VINDO AO ESTOQUE DE PEÇAS-------------------")

def cadrastar_Produto():
    global dadosDoEstoque
    global novoID 
    novoID = novoID + 1
    nome = input("\nDigite o nome do Produto: ")
    qntda = int(input("\nQual a quantidade do produto: "))
    localizacao = input("\nQual a localização da peça: ")

    produto = [novoID, nome, qntda, localizacao]
    dadosDoEstoque.append(produto)
    print("\nProduto cadastrado com sucesso!")
    travar_menu()

def listar_Estoque():
    global dadosDoEstoque
    print("\n________________ESTOQUE DE PEÇAS________________\n")
    print(dadosDoEstoque)
    travar_menu()

   
## Menu
while True: ## Rodar para sempre
    print("\nBem vindo ao estoque de peças, escolha uma opção:")
    print("1 - Cadrastar Produto | 2 - Listar os produtos | 3 - Buscar por ID | 4 - Alterar quantidade | 5 - Travar menu")
    opcao = input("Escolha uma opção: ")
    if (opcao == "1"):
        cadrastar_Produto()
    elif (opcao == "2"):
         listar_Estoque()     
    elif (opcao == "3"):
         buscar_ID()
    elif (opcao == "4"):
        alterar_quantidade()



    


