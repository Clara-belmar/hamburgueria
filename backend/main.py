from sanduiche import Lanche
from cardapio import Cardapio

resposta = "s"

#criando o objeto da classe Cardapio fora do laço
c = Cardapio()

while resposta == 's':

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

    resposta = input("Deseja continuar cadastrando lanches? (s/n) ")

c.exibirCardapio()