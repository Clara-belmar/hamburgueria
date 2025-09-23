class Bebida:
    def __init__(self, nome: str, preco: float, tamanho: str):
        self.nome = nome
        self.preco = preco
        self.tamanho = tamanho
    def exibirBebida(self):
        print (f"Bebida: {self.nome}, preço: {self.preco}, tamanho: {self.tamanho}")