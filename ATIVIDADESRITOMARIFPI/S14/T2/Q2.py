'''Escreva um programa que leia uma lista com 10 números reais, calcule e mostre a lista, a quantidade de números negativos e a soma dos números positivos dessa lista.'''

def numeros_negativos(lista):
    negativos = []
    for i in lista:
        if i < 0:
            negativos.append(i)
    return len(negativos)
        
def soma_positivos(lista):
    soma = 0
    for i in lista:
        if i > 0:
            soma += i
    return soma

      
def main():
    lista = []
    for i in range(10):
        numeros = float(input())
        lista.append(numeros)
        
    negativos = numeros_negativos(lista)
    soma = soma_positivos(lista)
    print(lista)
    print(negativos)
    print(soma)
        
if __name__ == '__main__':
    main()