class Lanche:
    def __init__(self,nome,preco,ingredientes):
        self.nome = nome
        self.preco = preco
        
        #verificação se "ingredientes" é uma lista
        
        if isinstance(ingredientes, str):
            self.ingredientes = [item.strip()
            for item in ingredientes.split(",")]
        else:
            self.ingredientes = ingredientes
    
    def convDic(self):
        """
        prepara o objeto para ser gravado no MongoDB,
        tornando-o um dicionario
        """
        return{
            "tipo":"lanche",
            "nome":self.nome,
            "preco":self.preco
        }
class Bebida:
    def __init__(self,nome,preco,tamanhoMl):
        self.nome = nome
        self.preco = preco
        self.tamanhoMl = tamanhoMl
    def convDic(self):
        """
        prepara o objeto para ser gravado no MongoDB,
        tornando-o um dicionario
        """
        return{
            "tipo":"bebida",
            "nome":self.nome,
            "preco":self.preco
        }