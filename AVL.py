from no_avl import Nodo
from tkinter import *

class AVL:
    def __init__(self):
        self.raiz = None


    def inserir(self, valor):
        self.raiz = self._inserir(self.raiz, valor)

    def _inserir(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        
        if valor < nodo.valor:
            nodo.esquerda = self._inserir(nodo.esquerda, valor)    
        elif valor > nodo.valor:
            nodo.direita = self._inserir(nodo.direita, valor)
        # return nodo
    
        # Atualizar o fator de balanceamento.
        balanceamento = self.fatorBalanceamento(nodo)
        print('Chave {}, Fator de balanceamento: {}\n'.format(valor.key,balanceamento))
        
        # Rotação Simples à Direita
        if balanceamento > 1 and valor.raiz < nodo.filho_da_esquerda.valor:
            return self.rotaDireita(nodo)
        # Rotação Simples à ESquerda.
        if balanceamento < -1 and valor.raiz > nodo.filho_da_direita.valor:
            return self.rotaEsquerda(nodo)
        # Rotação Dupla à Direita.
        if balanceamento > 1 and valor.raiz > nodo.filho_da_esquerda.valor:
            nodo.filho_da_esquerda = self.rotaEsquerda(nodo.filho_da_esquerda )
            return self.rotaDireita(nodo)
        # Rotação Dupla à Esquerda.
        if balanceamento < -1 and valor.raiz < nodo.filho_da_direita.valor:
            nodo.filho_da_direita = self.rotaDireita(nodo.filho_da_direita)
            return self.rotaEsquerda(nodo)
        return nodo
        
    # Calculo do Fator de Balanceamento.
    def fatorBalanceamento (self, raiz):
        if raiz != None:
            return self.altura(raiz.filho_da_esquerda) - self.altura(raiz.filho_da_direita)
        else:
            return 0
        
    # Rotação Simples à Direita
    def rotaDireita (self, raiz):
        aux = raiz.filho_da_esquerda
        raiz.filho_da_esquerda = aux.filho_da_direita
        aux.filho_da_direita = raiz
        raiz.altura = 1 + max(self.altura(raiz.filho_da_esquerda), self.altura(raiz.filho_da_direita))
        aux.altura = 1 + max(self.altura(aux.filho_da_esquerda), self.altura(aux.filho_da_direita))
        return aux
    
    # Rotação Simples à Esquerda
    def rotaEsquerda (self, raiz):
        aux = raiz.filho_da_direita
        raiz.filho_da_direita = aux.filho_da_esquerda
        aux.filho_da_esquerda = raiz
        raiz.altura = 1 + max(self.altura(raiz.filho_da_esquerda), self.altura(raiz.filho_da_direita))
        aux.altura = 1 + max(self.altura(aux.filho_da_esquerda), self.altura(aux.filho_da_direita))
        return aux
    
    def altura(self, nodo = None):
        if nodo is None:
            nodo = self.raiz
        alt_esquerda = 0
        alt_direita = 0
        if nodo.esquerda:
            alt_esquerda = self.altura(nodo.esquerda)
        if nodo.direita:
            alt_direita = self.altura(nodo.direita)
        if alt_direita > alt_esquerda:
            return alt_direita + 1
        return alt_esquerda + 1
    
    def min(self, nodo= None):
        if nodo == None:
            nodo = self.raiz
        if nodo is None:
            return nodo
        while nodo.esquerda:
            nodo = nodo.esquerda
        return nodo.valor
    
    def max(self, nodo= None):
        if nodo == None:
            nodo = self.raiz
        if nodo is None:
            return nodo
        while nodo.direita:
            nodo = nodo.direita
        return nodo.valor


    def exibir_arvore_tkinter(self):
            root = Tk()
            canvas = Canvas(root, width=800, height=600)
            canvas.pack()
            self._exibir_nodo_tkinter(self.raiz, 400, 50, 200, canvas)
            root.mainloop()

    def _exibir_nodo_tkinter(self, nodo, x, y, espacamento, canvas):
        if nodo:
            canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="white", outline="black")
            canvas.create_text(x, y, text=str(nodo.valor))

            if nodo.esquerda:
                canvas.create_line(x - 20, y, x - espacamento, y + 50, fill="black")
                self._exibir_nodo_tkinter(nodo.esquerda, x - espacamento, y + 50, espacamento // 2, canvas)

            if nodo.direita:
                canvas.create_line(x + 20, y, x + espacamento, y + 50, fill="black")
                self._exibir_nodo_tkinter(nodo.direita, x + espacamento, y + 50, espacamento // 2, canvas)


if __name__ == "__main__":
    arvore = AVL()
    arvore.inserir(1)
    arvore.inserir(2)
    arvore.inserir(3)
    arvore.inserir(-1)
    arvore.inserir(-2)

    # print( arvore.altura(arvore.raiz.esquerda))
    print(arvore.min())
    print(arvore.max())

    arvore.exibir_arvore_tkinter()