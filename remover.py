from arvore_avl import ArvoreAVL, No
# from arvore_avl import ArvoreAVL, No
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

# def exeplo_arvore(size=42):
#     valores=[61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
#     arvore = ArvoreAVL()
#     for v in valores:
#         arvore.inserir(v)
#     return arvore

# def extend_arvore(size=42):
#     valores=[61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 100, 90]
#     arvore = ArvoreAVL()
#     for v in valores:
#         arvore.inserir(v)
#     return arvore

# bst = extend_arvore()
# print("Percuso em ordem")
# bst.inOrdem()
# print()
# print('-----')
# print("Percuso em nível")
# bst.percurso_em_nivel()

# print()
# v = 61
# bst.remove(v)
# print("Após remover {}".format(v))
# bst.inOrdem()
# print()
# print()
# print("Percuso em ordem")
# bst.inOrdem()
# print()
# print('-----')
# print("Percuso em nível")
# bst.percurso_em_nivel()

# print()
# print('~=~=~=~=')
# print("Altura: ", bst.altura())
# print('~=~=~=~=')
# print()
# print("Menor: ", bst.min())
# print()
# print('~=~=~=~=')
# print("Maior: ", bst.max())

# if __name__ == "__main__":
#     arvore = ArvoreAVL()
        
#     while True:
#         print('========  OPÇÔES ===========')
#         print('Digite 1 para inserir um elemento! ')
#         print('Digite 2 para remover um elemento! ')
#         print('Digite 3 para buscar um elemento! ')
#         print('Digite 4 para Imprimir a arvore! ')
#         print('Digite 0 para sair! ')
#         print('===========================')
#         print("")
#         print("")
#         op = int(input("Digite um número conforme a opão desejada! "))
        
#         if op == 1:
#             # v = int(input("Informe o valor que desena add na árvore: "))
#             arvore.inserir(10)
#         elif op == 2:
#             arvore.remove()
#         elif op == 3:
#             arvore.busca()
#         elif op == 4:
#             arvore.inOrdem()
#         elif op == 0:
#             break
            
   


    
      