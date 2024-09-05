'''Escreva um programa que leia uma lista com 20 números inteiros. Escreva os elementos da lista eliminando elementos repetidos.'''
def lista_sem_duplicados(lista):
    nova_lista = []
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista


def main():
    lista = []
    for i in range(20):
        numero = int(input())
        lista.append(numero)
    
    nova_lista = lista_sem_duplicados(lista)
    print(nova_lista)
    
if __name__ == '__main__':
    main()