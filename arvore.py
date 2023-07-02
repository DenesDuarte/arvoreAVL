ROOT = "root"
from fila import Fila
from no import No
class ArvoreBinaria:
   
    def __init__(self, dado = None, no=None):
        if no:
            self.root = no
        elif dado:
            no = No(dado)
            self.root = no
        else:
            self.root = None
            
    
    # Percurso em Pré-ordem !
    def preOrdem(self, no=None):
        if no is None:
            no = self.root
        print(no, end=' ')
        if no.filho_da_esquerda:
            self.preOrdem(no.filho_da_esquerda)
        if no.filho_da_direita:
            self.preOrdem(no.filho_da_direita)
          
    # def preOrdem(self, no=None):
    #     if no is None:
    #         no = self.root
    #     print(self.value, end=' ')
        
    #     if no.filho_da_esquerda:
    #         self.no.filho_da_esquerda.preOrdem()
    #     if no.filho_da_direita:
    #         self.no.filho_da_direita.preOrdem()
            
      
        
    # Percurso em ordem simétrica!
    def inOrdem(self, no=None):
        if no is None:
            no = self.root
        if no.filho_da_esquerda:
            self.inOrdem(no.filho_da_esquerda)
        print(no, end=' ')
        if no.filho_da_direita:
            self.inOrdem(no.filho_da_direita)
            
    # Percurso em Pós-ordem!
    def posOrdem(self, no=None):
        if no is None:
            no = self.root
        if no.filho_da_esquerda:
            self.posOrdem(no.filho_da_esquerda)
        if no.filho_da_direita:
            self.posOrdem(no.filho_da_direita)
        print(no, end='')
    
    def altura(self, no=None):
        if no is None:
            no = self.root
        alt_esquerda = 0
        alt_direita = 0
        if no.filho_da_esquerda:
            alt_esquerda = self.altura(no.filho_da_esquerda)
        if no.filho_da_direita:
            alt_direita = self.altura(no.filho_da_direita)
        if alt_direita > alt_esquerda:
            return alt_direita + 1
        return alt_esquerda + 1
        

    def percurso_em_nivel(self, no=ROOT):
        if no == ROOT:
            no = self.root
        
        fila = Fila()
        fila.push(no)
        while len(fila):
            no = fila.pop()
            if no.filho_da_esquerda:
                fila.push(no.filho_da_esquerda)
            if no.filho_da_direita:
                fila.push(no.filho_da_direita)
            print(no, end=" ")

# if __name__ == "__main__":
#     arvore = ArvoreBinaria(10)
    
#     arvore.root.filho_da_esquerda = No(20)
#     arvore.root.filho_da_direita = No(14)
    
#     print(arvore.root)
#     print(arvore.root.filho_da_direita)
#     print(arvore.root.filho_da_esquerda)
    