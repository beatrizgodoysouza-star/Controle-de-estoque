dadosDoEstoque = [
    [0, "Martelo", 23, 34],
    [1, "Rosca", 21, 89],
    [2, "Engrenagem", 34, 4]
] ## ID, Nome, quantidade, localização
novoID = 2

print("------------------SEJA BEM-VINDO AO ESTOQUE DE PEÇAS-------------------")

##Função inicial para cadrastrar uma peça desejada
def cadrastar_Produto():
    global dadosDoEstoque
    global novoID 
    novoID = novoID + 1 #Aumenta automaticamente o ID a cada peça adicionada
    nome = input("\nDigite o nome do Produto: ")
    qntda = int(input("\nQual a quantidade do produto: "))
    localizacao = input("\nQual a localização da peça: ")

    produto = [novoID, nome, qntda, localizacao]
    dadosDoEstoque.append(produto)
    print("\nProduto cadastrado com sucesso!")
    travar_menu()

#Lista o estoque
def listar_Estoque():
    global dadosDoEstoque
    print("\n________________ESTOQUE DE PEÇAS________________\n")
    print(dadosDoEstoque)
    travar_menu()

#Função para procurar uma peça através do ID
def buscar_ID():
    posicaoProcurada = -1
    id_procurado = int(input("\nDigite o ID do produto que deseja buscar: "))
    for i in range(len(dadosDoEstoque)):
        if(dadosDoEstoque[i][0] == id_procurado):
            posicaoProcurada = i #Fala que o produto esta na linha 

    if posicaoProcurada == -1: #Caso a posição seja errada, o sistema avisa
        print("Não existe esse ID")
    else:
        print(dadosDoEstoque[posicaoProcurada])
    travar_menu()

def alterar_quantidade():
    id_procurado = int(input("\nDigite o ID do produto que deseja alterar a quantidade: "))
    
    for i in range(len(dadosDoEstoque)):
        if dadosDoEstoque[i][0] == id_procurado: #[i] é a peça e [0] é a posição
            print(f"\nProduto encontrado: {dadosDoEstoque[i][1]}") 
            print(f"Quantidade atual: {dadosDoEstoque[i][2]}")
            
            # Pede a nova quantidade
            nova_qtd = int(input("Digite a nova quantidade: ")) #Adiciona a nova quantidade
            
            # Atualiza o valor na lista
            dadosDoEstoque[i][2] = nova_qtd #muda a coluna 2 do produto desejado
            print("\n Quantidade atualizada!")
            
            if nova_qtd <= 0: # Se a qauntidade for qualquer número menor ou igual a 0, o sistema automaticamente exclui da lista, mostrando que não tem mais no estoque
                dadosDoEstoque.pop(i)
                print("O produto foi removido do estoque!")
            break
    travar_menu()
    
def travar_menu(): #Função para travar o menu e ele não continuar aparecendo como um loop 
    input("\nPressione ENTER para continuar...\n")

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
    elif (opcao == "5"):
        travar_menu()
    break


    


