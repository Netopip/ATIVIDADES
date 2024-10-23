'''Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado'''

def main():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            n = int(input(f'Digite um valor para a posição {i,j}:'))
            linha.append(n)
        matriz.append(linha)
        
    for linha in matriz:
        
        print(linha)

if __name__== '__main__':
    main()
'''
import numpy as np

matriz = np.identity(5)
#matriz[0,0]=6
#matriz[0][0] = 6 || as duas formas de acessar um valor estão corretas
print(matriz)
'''


