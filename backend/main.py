from sanduiche import Cardapio
from cardapio import Lanche

ingredientes=[]

nome = input("Nome do novo lanche: ")
preco = float(input("Insira o preço: "))

for item in range(6):
    ingrediente = input(f"informe o ingrediente {item+1}: ")
    ingredientes.append(ingrediente)

lanche1 = Cardapio('Egg-Burger',24.99,['pão com gergelim', 'queijo parmesão', 'ovo', 'hamburguer'])
lanche2 = Cardapio('Hot-dog New York Style',35.50, ['pão', 'salsicha de bife', 'molho de cebola', 'chucrute', 'mostarda marrom ardida'])
lanche3 = Cardapio('X-Tudo', 25.99, ['pão', 'milho', 'queijo parmesão', 'brócoles', 'couve-flor', 'hamburguer', 'maionese verde', 'bacon', 'ovo', 'presunto'])
l = Cardapio(nome,preco,ingredientes)

print(f"Nome:{lanche1.nome}; Preço:{lanche1.preco}; Ingredientes: {lanche1.ingredientes}")
print(f"Nome:{lanche2.nome}; Preço:{lanche2.preco}; Ingredientes: {lanche2.ingredientes}")
print(f"Nome:{lanche3.nome}; Preço:{lanche3.preco}; Ingredientes: {lanche3.ingredientes}")
print(f"Nome:{l.nome}; Preço:{l.preco}; Ingredientes: {l.ingredientes}")