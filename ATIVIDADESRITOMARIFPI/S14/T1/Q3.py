'''Dadas duas listas A e B contendo 20 elementos inteiros cada, gerar e exibir uma lista C do mesmo tamanho cujos elementos sejam a soma dos respectivos elementos de A e B.'''


def criar_lista_c(lista_A, lista_B):
    lista_C = []
    for i in range(20):
        lista_C.append(lista_A[i] + lista_B[i])
    return lista_C

def main():
    lista_A = []
    for i in range(20):
        numero = int(input())
        lista_A.append(numero)
    lista_B = []
    for i in range(20):
        numero1= int(input())
        lista_B.append(numero1)
    lista_C = criar_lista_c(lista_A, lista_B)
    print(f'{lista_A}\n{lista_B}')
    print(lista_C)

if __name__ == '__main__':
    main()