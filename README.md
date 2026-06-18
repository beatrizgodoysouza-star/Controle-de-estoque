## Sistema de controle de estoque (Introdução)

Esse é um sistema interativo em Pyton para gerenciar o estoque de peças de alguma empresa industrial. O programa roda direto no terminal e permite que cadastre novas peças, ache rapidamente peças por ID, consegue atualizar a quantidade de peças (caso aumente ou diminua no estoque real) e remove itens quando o necessário (caso não tenha mais peças)

## Funcionalidades do sistema (Como funciona cada Função)
->Cadastrar Produto: Tem a função de adicionar um novo produto ao sistema, pedindo apenas o nome, quantidade, localização e o ID é colocado pelo sistema (em ordem de cadastro),assim indicando que a peça foi cadastrada com sucesso.
->Listar estoque: Sua função é mostrar todos os itens da matriz/estoque em ordem de cadrasto e todas as informações necessárias.
->Buscar ID: A função tem como objetivo de perguntar o ID da peça desejada e assim que escrevê-la, mostrar a linha inteira com todas suas informações individuais.
->Alterar quantidade: Essa função serve para mudar a quantidade de produto do estoque conforme ela mudar na vida real. Ela pergunta qual o ID da peça que você quer trocar a quantidade, em seguida mostra o nome da peça, a quantidade que tem e pergunta qual vai ser a quantidade atual. Quando der ENTER ele mostra que a quantidade foi mudada. Mas, caso o usuário coloque número 0 ou número negativo, o sistema automaticamente exclui do estoque por ser um número menor e igual a 0
->Travar Menu: Essa função faz com que pare com as perguntas e só continua fazendo-as caso o usuário aperte ENTER, caso não aperte, o sistema vai ficar travado.

## Menu
**Opção 1: tem a funcionalidade de cadastrar um novo produto
**Opção 2: tem a funcionalidade de listar todos os produtos do estoque
**Opção 3: tem a funcionalidade de buscar um item por ID
**Opção 4: tem a funcionalidade de mudar a quantidade de peças
**Opção 5: tem a funcionalidade de travar o menu para que não fique no loop eterno
