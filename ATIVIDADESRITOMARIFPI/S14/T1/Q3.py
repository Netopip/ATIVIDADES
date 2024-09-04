'''Dadas duas listas A e B contendo 20 elementos inteiros cada, gerar e exibir uma lista C do mesmo tamanho cujos elementos sejam a soma dos respectivos elementos de A e B.'''


def main():
    lista_A = []
    for i in range(20):
        numero = int(input())
        lista_A.append(numero)
    lista_B = []
    for i in range(20):
        numero1= int(input())
        lista_B.append(numero1)
    print(lista_A,lista_B)

if __name__ == '__main__':
    main()