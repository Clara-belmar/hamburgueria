class Lanche:
    def __init__(self,nome,preco,ingredientes):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes
    def exibirLanche(self):
        print(f"Lanche: {self.nome}; Preço: {self.preco}; Ingredientes: {self.ingresientes}")