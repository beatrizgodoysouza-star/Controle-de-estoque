dadosDoEstoque = [
    [0, "Martelo", 23, 34],
    [1, "Rosca", 21, 89],
    [2, "Engrenagem", 34, 4]
] ## ID, Nome, quantidade, localização
novoID = 2


   
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



    


