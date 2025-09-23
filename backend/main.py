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
        nome = input("Nome do novo lanche: ")
        preco = float(input("Insira o preço: "))
        qtdeIngredientes = int(input("Escreva quantos ingredientes você quer adicionar: "))
        for i in range(qtdeIngredientes):
            ingrediente = input(f"informe o ingrediente {i+1}: ")
            ingredientes.append(ingrediente)

        #criando o objeto da classe Lanche dentro do laço
        l = Lanche(nome,preco,ingredientes)

        #adicionando o lanche "l" ao cardapio "c"
        c.adicionarItem(l)
    elif opcao == 2:
        nome = input("Nome da nova bebida: ")
        preco = float(input("Insira o preço: "))
        tamanho = input("qual é o tamanho? ")
        b = Bebida(nome, preco, tamanho)

    resposta = input("Deseja continuar cadastrando no Cadápio? (s/n) ")

c.exibirCardapio()