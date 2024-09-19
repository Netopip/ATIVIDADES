'''Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles. Considere que todos os valores são diferentes. NÃO use as funções min() e max().'''
def maior_menor(lista):
    maior = menor = lista[0]
    
    for i in lista:
        if i > maior:
            maior = i
        elif i < menor:
            menor = i
    return maior, menor
def main():
    lista = []
    for i in range(5):
        n = int(input())
        lista.append(n)
        
    
    maior, menor = maior_menor(lista)
    print(f'{maior}\n{menor}')
    
if __name__ == '__main__':
    main()