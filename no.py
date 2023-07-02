class No:
    def __init__(self, dado):
        self.dado = dado
        self.setFilhos(None, None)
        self.altura = 1
        
    def  setFilhos ( self , filho_da_esquerda , filho_da_direita ):
        self.filho_da_esquerda  =  filho_da_esquerda
        self.filho_da_direita  =  filho_da_direita
        
    def __str__(self):
        return str(self.dado)


    