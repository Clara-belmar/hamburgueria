from sanduiche import Cardapio
from cardapio import Lanche

resposta = 's'

while resposta == 's':

    ingredientes=[]

    nome = input("Nome do novo lanche: ")
    preco = float(input("Insira o preço: "))

    for i in range(4):
        ingrediente = input(f"informe o ingrediente {i+1}: ")
        ingredientes.append(ingrediente)

    #lanche1 = Cardapio('Egg-Burger',24.99,['pão com gergelim', 'queijo parmesão', 'ovo', 'hamburguer'])
    #lanche2 = Cardapio('Hot-dog New York Style',35.50, ['pão', 'salsicha de bife', 'molho de cebola', 'chucrute', 'mostarda marrom ardida'])
    #lanche3 = Cardapio('X-Tudo', 25.99, ['pão', 'milho', 'queijo parmesão', 'brócoles', 'couve-flor', 'hamburguer', 'maionese verde', 'bacon', 'ovo', 'presunto'])
    l = Cardapio(nome,preco,ingredientes)

    print(f"Nome:{l.nome}; Preço:{l.preco}; Ingredientes: {l.ingredientes}")
    
    c = Lanche()
    c.adicionarItem(l)

    resposta = input("Deseja continuar cadastrando lanches? (s/n) ")
print(f"Cardápio: {c.itens})