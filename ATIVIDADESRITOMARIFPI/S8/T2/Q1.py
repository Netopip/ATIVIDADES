'''Escreva um programa que leia um número inteiro e some 5 caso valor lido seja par ou some 8 caso o valor lido seja ímpar. Mostre na tela o resultado da operação.'''
def somar_valor(n):
    if n %2 == 0:
        print(n + 5)
    else: 
        print(n + 8)

def main():
    valor = int(input())
    
    somar_valor(valor)
    
if __name__ == '__main__':
    main()