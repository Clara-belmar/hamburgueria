class Cardapio:
    def __init__(self):
        self.item = []
        self.categoria = ""
    
    def adicionarItem(self,item):
        self.item.append(item)
    
    def __str__(self):
        return f"Item{self.item};"
    def exibirCardapio(self):
        for item in self.item:
            item.exibirLanche