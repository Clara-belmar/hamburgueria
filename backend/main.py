from sanduiche import Lanche
from cardapio import Cardapio
from bebida import Bebida

resposta = "s"

#criando o objeto da classe Cardapio fora do laço
c = Cardapio()

while resposta == 's':
    print ("Gerenciando cardápio")
    print ("1-Adicionar lanche")
    print ("2-Adicionar bebida")
    print ("3-Exibir cardapio")
    print ("4-Sair")
    opcao = int(input("Escolha uma das opções acima: "))
    if opcao == 1:
        ingredientes=[]
        categoria = input("Insira a categoria: ")
        nome = input("Nome do novo lanche: ")
        preco = float(input("Insira o preço: "))
        qtdeIngredientes = int(input("Escreva quantos ingredientes você quer adicionar: "))
        for i in range(qtdeIngredientes):
            ingrediente = input(f"informe o ingrediente {i+1}: ")
            ingredientes.append(ingrediente)

        #criando o objeto da classe Lanche dentro do laço
        l = Lanche(nome,preco,ingredientes)

        #adicionando o lanche "l" ao cardapio "c"
        c.adicionarItem(l, categoria)
    elif opcao == 2:
        categoria = input("Insira a categoria: ")
        nome = input("Nome da nova bebida: ")
        preco = float(input("Insira o preço: "))
        tamanho = input("Qual é o tamanho? ")
        
        b = Bebida(nome, preco, tamanho)
        
        c.adicionarItem(b, categoria)
    elif opcao == 3:
        c.exibirCardapio()
    else:
        resposta = input("Deseja continuar? (s/n) ")
