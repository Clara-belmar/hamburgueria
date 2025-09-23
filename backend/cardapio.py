from sanduiche import Lanche
from bebida import Bebida
class Cardapio:
    def __init__(self):
        self.categoria = ""
    
    def adicionarItem(self,item,categoria):
        self.item.append(item)
        self.categoria = categoria

    def exibirCardapio(self):
        for item in self.item: 
            if self.categoria == "lanche":
                item.exibirLanche()
            elif self.categoria == "bebida":
                item.exibirBebida()