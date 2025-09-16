class Lanche:
    def __init__(self):
        self.itens = []
        self.categoria = ""
    
    def adicionarItem(self, item):
        self.itens.append(item)
    
    def __str__(self):
        return f"Item{self.itens};"