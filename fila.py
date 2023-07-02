class No:
    # Construtor
    def __init__(self,valor):
        self.valor = valor
        self.proximo = None

    
class Fila:
    # Construtor
    def __init__(self):
        self.primeiroElemento = None
        self.utimoElemento = None
        self._size = 0


    def push(self, elemento):
        # Add elementos na fila.
        no = No(elemento)
        # chegando um elemento vou verificar se a fila tem um útimo elemento caso esteja vasia:
        if self.utimoElemento is None:
            self.utimoElemento = no
        # se já existi algem na utima posição (esse elemento tera que saber que chegou algém atrá dele)
        else:
            self.utimoElemento.proximo = no
            self.utimoElemento = no
        # se a fila estiver vasia o 1° e o útimo elemento recebem o mesmo valor
        if self.primeiroElemento is None:
            self.primeiroElemento = no

        self._size += 1


    def pop(self):
        # Remove o elemento do inicio da fila.
        if self._size > 0:
            elemento = self.primeiroElemento.valor
            self.primeiroElemento = self.primeiroElemento.proximo
            self._size -= 1
            return elemento
        raise ImportError("A lista está vazia!")

    def peek(self):
        # Retorna o elemento do topo sem remover.
        if self._size > 0:
            elemento = self.primeiroElemento.valor
            return elemento
        raise ImportError("A lista está vazia!")
          
        
    def __len__(self):
        """Retorna a qtd de elementos da fila"""
        return self._size

    def __repr__(self):
        if self._size > 0:
            r = ""
            ponteiro = self.primeiroElemento
            while(ponteiro):
                r = r + str(ponteiro.valor) + " "

                ponteiro = ponteiro.proximo
            return r
        return "A fila está vazia!"


    
    def __str__(self):
        # Mostra a converção do elemento para estring
        return self.__repr__()

    def mostrarFila(self):
        f = self.primeiroElemento
        while f is not None:
            print(f'{f.valor}', end = ", ")

            f = f.proximo

        
# f = Fila()
# print(f'Tamanho da fila: {len(f)}')

# f.push("Denes")
# f.push(25)
# f.push("Pietro")
# f.push(0.6)

# f.pop()
# f.pop()
# # f.pop()
# # f.pop()
# print(f'O 1° elemento da fila é: {f.peek()}')

# print(f'Tamanho da fila: {len(f)}')
# print("#################")
# print(f.mostrarFila())