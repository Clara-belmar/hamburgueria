class ItemCardapio:
    def __init__ (self, nome, preco):
        self.nome = nome
        self.preco = preco
    def exibirItem(self):
        print(f"Item:{self.nome}, preço: {self.preco}")