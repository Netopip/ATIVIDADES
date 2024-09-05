'''Escreva um programa que leia 10 números inteiros e os armazene em uma lista. Imprima a lista, o maior elemento e a pos'''

def maior_elemento(lista):
    maior = lista[0]
    indice = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indice = i
            
    return maior,indice
        

def main():
    lista = []
    for i in range(10):
        numero = int(input())
        lista.append(numero)
        
    maior, indice = maior_elemento(lista)
    print(lista)
    print(maior)
    print(indice)
    
    
if __name__ == '__main__':
    main()