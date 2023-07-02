from arvore_avl import ArvoreAVL, No
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

def in_ordem_exemplo_arvore():
    arvore = ArvoreAVL()
    n1 = No('11')
    n2 = No('16')
    n3 = No('32')
    n4 = No('43')
    n5 = No('51')
    n6 = No('55')
    n8 = No('66')
    n9 = No('77')
    n10 = No('79')
    n11 = No('82')
    n12 = No('89')
    # n13 = No('90')
    n14 = No('100')
    n0 = No('61')
    
    n0.filho_da_esquerda = n4
    n0.filho_da_direita = n12
    n4.filho_da_esquerda = n2
    n4.filho_da_direita = n5
    n2.filho_da_esquerda = n1
    n2.filho_da_direita = n3
    n5.filho_da_direita = n6
    n12.filho_da_esquerda = n8
    n12.filho_da_direita = n14
    n8.filho_da_direita = n10
    n10.filho_da_esquerda = n9
    n10.filho_da_direita = n11
    # n14.filho_da_esquerda = n13
    #Raiz da árvore
    arvore.root = n0
    return arvore
    
if __name__ == "__main__":
    arvore = in_ordem_exemplo_arvore()
    print('Percuso em ordem:')
    arvore.inOrdem()
    print()
    print("Altura: ", arvore.altura())