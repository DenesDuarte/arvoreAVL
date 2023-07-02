# from arvore import ArvoreBinaria, No
from arvore_avl import ArvoreAVL, No
# from no import No
###############################################################

# Testando 
#                       '61'
#                     /     \
#                '43'         '89'
#                /   \         /   \
#            '16'    '51'   '66'      '100'
#           /   \       \     \        /
#          /     \       \     \      /
#       '11'    '32'    '55'   '79'  '90'
#                             /   \
#                          '77'   '82'

# def exeplo_arvore():
#     valores=[61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
#     arvore = ArvoreBinaria()
#     for v in valores:
#         arvore.inserir(v)
#     return arvore

# def extend_arvore():
#     valores=[61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 100, 90]
#     arvore = ArvoreBinaria()
#     for v in valores:
#         arvore.inserir(v)
#     return arvore

# bst = extend_arvore()
# bst.inOrdem()
# print()

# v = 11
# bst.remove(v)
# print("Após remover {}".format(v))
# bst.inOrdem()
      

def exemplo_arvore():
    arvore = ArvoreAVL()
    n1 = No('43')
    n2 = No('16')
    n3 = No('51')
    n4 = No('11')
    n5 = No('32')
    n6 = No('55')
    n7 = No('89')
    n8 = No('66')
    n9 = No('79')
    n10 = No('77')
    n11 = No('82')
    n12 = No('100')
    n13 = No('90')
    n0 = No('61')
    
    n0.filho_da_esquerda = n1
    n0.filho_da_direita = n7
    n1.filho_da_esquerda = n2
    n1.filho_da_direita = n3
    n2.filho_da_esquerda = n4
    n2.filho_da_direita = n5
    n3.filho_da_direita = n6
    n7.filho_da_esquerda = n8
    n7.filho_da_direita = n12
    n8.filho_da_direita = n9
    n9.filho_da_esquerda = n10
    n9.filho_da_direita = n11
    n12.filho_da_esquerda = n13
    #Raiz da árvore
    arvore.root = n0
    # arvore.root = n7
    return arvore
    
if __name__ == "__main__":
    arvore = exemplo_arvore()
    print('Percuso em ordem:')
    arvore.inOrdem()
    print()
    print('~=~=~=~=')
    print("Altura: ", arvore.altura())
    print('~=~=~=~=')
    print()
    print("Mínimo: ", arvore.min())
    print()
    print('~=~=~=~=')
    print("Máximo: ", arvore.max())
   

