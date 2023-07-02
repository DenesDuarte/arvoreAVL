ROOT = "root"  
from no import No
# from fila import Fila
from arvore import ArvoreBinaria
import random

    
# Passando a "ArvoreBinaria" como parametro da nossa "ArvoreBinariaDeBusca" assim ela já erdará tudo da mesma.
class ArvoreAVL(ArvoreBinaria):
    # def inserir (self,valor, no):
    #     pai = None
    #     alx = self.root
    #     while (alx):
    #         pai = alx
    #         if valor < alx.dado:
    #             alx = alx.filho_da_esquerda
    #         else:
    #             alx = alx.filho_da_direita
    #     if pai is None:
    #         self.root = No(valor)
    #     elif valor < pai.dado:
    #         pai.filho_da_esquerda = No(valor)
    #     else:
    #         pai.filho_da_direita = No(valor)
        
    def inserir (self, valor):
        # self.root = self._inserir(self.root, valor)
        return self._inserir(self.root, valor)
   
    def _inserir (self, no, valor):
        if no is None:
            return No(valor)
        # Inserção recursiva
        elif valor < no.valor:
            no.filho_da_esquerda = self._inserir(no.filho_da_esquerda, valor)
        else:
            no.filho_da_direita = self._inserir(no.filho_da_direita, valor)
        
        # Atualizar a altura do nó!
        no.altura = 1 + max(self._get_altura(no.filho_da_esquerda), self._get_altura(no.filho_da_direita))
        
        # Verificar o fator de balanceamento e realizar as rotações se necessário
        f_balanceamento = self._get_f_balanceamento(no)
        
        if f_balanceamento > 1 and valor < no.filho_da_esquerda.valor:
            return self._rotacao_direita(no)
        
        if f_balanceamento < -1 and valor > no.filho_da_direita.valor:
            return self._rotacao_esquerda(no)
        
        if f_balanceamento > 1 and valor > no.filho_da_esquerda.valor:
            no.filho_da_esquerda = self._rotacao_esquerda(no.filho_da_esquerda )
            return self._rotacao_direita(no)
        
        if f_balanceamento < -1 and valor < no.filho_da_direita.valor:
            no.filho_da_direita = self._rotacao_direita(no.filho_da_direita)
            return self._rotacao_esquerda(no)
        
        return no
    
     #*** busca sem valor padrão
    def busca(self, valor):
        return self._busca(valor, self.root)

    def _busca (self, valor, no):
        if no is None:
            return no
        if no.dado == valor:
            return ArvoreAVL(no)
        if valor < no.dado:
            return self._busca(valor, no.filho_da_esquerda)
        return self._busca(valor, no.filho_da_direita)
    
    
    
    #  *** Busca com valor padrão
    # def busca (self, valor, no=0):
    #     if no == 0:
    #         no = self.root
    #     if no is None or no.dado == valor:
    #         return ArvoreBinariaDeBusca(no)
    #     if valor < no.dado:
    #         return self.busca(valor, no.filho_da_esquerda)
    #     return self.busca(valor, no.filho_da_direita) 
    
    def min(self, no= ROOT):
        if no is None:
            return no
        if no == ROOT:
            no = self.root
        while no.filho_da_esquerda:
            no = no.filho_da_esquerda
        return no.dado
    
    def max(self, no=ROOT):
        if no is None:
            return no
        if no == ROOT:
            no = self.root
        while no.filho_da_direita:
            no = no.filho_da_direita
        return no.dado
    #################### REMOVER #####################
    # def remove(self, valor, no=ROOT):
    #     if no == ROOT:
    #         no = self.root
    #     if no is None:
    #         return no
    #     if valor < no.dado:
    #         no.filho_da_esquerda = self.remove(valor, no.filho_da_esquerda)
    #     elif valor > no.dado:
    #         no.filho_da_direita = self.remove(valor, no.filho_da_direita)
    #     else:
    #         if no.filho_da_esquerda is None:
    #             return no.filho_da_direita
    #         elif no.filho_da_direita is None:
    #             return no.filho_da_esquerda
    #         else:
    #             sucessor = self.min(no.filho_da_direita)
    #             no.dado = sucessor
    #             no.filho_da_direita = self.remove(sucessor, no.filho_da_direita)
                
    #     return no
    
    def remove(self, dado):
        self.root = self._remove(self.root, dado)
        
    def _remove(self, no, dado):
        if no == ROOT:
            no = self.root
        if no is None:
            return no
        # Remoção recursiva
        if dado < no.dado:
            no.filho_da_esquerda = self.remove(no.filho_da_esquerda, dado)
        elif dado > no.dado:
            no.filho_da_direita = self.remove(no.filho_da_direita, dado)
        else:
            # Nó encontrado, realizar a remoção
            if no.filho_da_esquerda is None:
                sucessor = no.filho_da_direita
                no = None
                return sucessor
            elif no.filho_da_direita is None:
                sucessor = no.filho_da_esquerda
                no = None
                return sucessor
            
            sucessor = self.menor(no.filho_da_direita)
            no.dado = sucessor.dado
            no.filho_da_direita = self.remove(no.filho_da_direita, sucessor.dado)
            
        if no is None:
            return no
        
        # Atualizar a altura do nó
        no.altura = 1 + max(self._get_altura(no.filho_da_esquerda), self._get_altura(no.filho_da_direita))

        # Verificar o fator de balanceamento e realizar as rotações se necessário
        f_balanceamento = self._get_f_balanceamento(no)
        
        if f_balanceamento > 1 and self._get_f_balanceamento(no.filho_da_esquerda) >= 0:
            return self._rotacao_direita(no)
        
        if f_balanceamento < -1 and self._get_f_balanceamento(no.filho_da_direita) <= 0:
            return self._rotacao_esquerda(no)
          
        if f_balanceamento > 1 and self._get_f_balanceamento(no.filho_da_esquerda) < 0:
            no.filho_da_esquerda = self._rotacao_esquerda(no.filho_da_esquerda )
            return self._rotacao_direita(no)
        
        if f_balanceamento < -1 and self._get_f_balanceamento(no.filho_da_direita) > 0:
            no.filho_da_direita = self._rotacao_direita(no.filho_da_direita)
            return self._rotacao_esquerda(no)
            
        return no
    
        
    # def _rotacao_esquerda(self, z):
    #     y = z.direita
    #     T2 = y.esquerda
        
    #     # Realizar a rotação à esquerda
    #     y.esquerda = z
    #     z.direita = T2
        
    #     # Atualizar as alturas dos nós envolvidos na rotação
    #     z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
    #     y.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(y.direita))
    def _rotacao_esquerda(self, z):
        y = z.filho_da_direita
        T2 = y.filho_da_esquerda
        
        # Realizar a rotação à esquerda
        y.filho_da_esquerda = z
        z.filho_da_direita = T2
        
        # Atualizar as alturas dos nós envolvidos na rotação
        z.altura = 1 + max(self._get_altura(z.filho_da_esquerda), self._get_altura(z.filho_da_direita))
        y.altura = 1 + max(self._get_altura(z.filho_da_esquerda), self._get_altura(y.filho_da_direita))
        
        return y
    
    # def _rotacao_direita(self, z):
    #     y = z.esquerda
    #     T3 = y.direita
        
    #     # Realizar a rotação à direita
    #     y.direita = z
    #     z.esquerda = T3
        
    #     # Atualizar as alturas dos nós envolvidos na rotação
    #     z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
    #     y.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(y.direita))
        
    #     return y
    def _rotacao_direita(self, z):
        y = z.filho_da_esquerda
        T3 = y.filho_da_direita
        
        # Realizar a rotação à direita
        y.filho_da_direita = z
        z.filho_da_esquerda = T3
        
        # Atualizar as alturas dos nós envolvidos na rotação
        z.altura = 1 + max(self._get_altura(z.filho_da_esquerda), self._get_altura(z.filho_da_direita))
        y.altura = 1 + max(self._get_altura(z.filho_da_esquerda), self._get_altura(y.filho_da_direita))
        
        return y
       
        
    
    

          
       
    
    
            
 