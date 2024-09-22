import numpy as np

minha_lista = [0,1,2,3,4,5]
meu_array = np.array([0,1,2,3,4,5])
'''
print(type(meu_array))
print(type(minha_lista))

# fazer operação de soma na lista:
#print(minha_lista + 1) causara um erro
#fazer operação de soma com array:
print(meu_array + 1)

# soma de duas listas:
print(minha_lista + minha_lista)

#soma de duas arrays:
print(meu_array + meu_array)

# subtrari um array:
print(meu_array- meu_array)

#multiplicação:
print(minha_lista * 2 )
print(meu_array * 2)

#divisão:
#print(minha_lista / 2) causara um erro
print(meu_array / 2)
'''
#matrizes:
matrix_1 = np.array([minha_lista, minha_lista, minha_lista])
#print(matrix_1)
matrix_2 = np.array([meu_array, meu_array, meu_array])
#print(matrix_2)
#matriz_3 = np.array([[1,2],[1,2],[1,2,3]])
#print(matriz_3) dara erro

#cirando matrizes zeradas:
matriz_4 = np.zeros((6,6)) #cria uma matriz de 6 linhas e 6 colunas com todos os valores zerados
#print(matriz_4)

#operação de soma de matrizes:

print(matrix_2 + 3)

#subtração
print(matrix_2 - 3)

#multipliacação:
print(matrix_2 * 2)

#divisão:
print(matrix_2 / matrix_2)

#dados em arrays:
print(meu_array)
print(meu_array[3])
print(meu_array[-1])
meu_array[0] = 6
print(meu_array)

#dados de matrizes:
print(matrix_2)
print(f'O valor da matriz 2 no pontos 2,3 é : {matrix_2[2,3]}') 
print(f'O valor da matriz 2 do ultimo numero da linha 1 é : {matrix_2[1,-1]}')
matrix_2[0,0] = 6
print(matrix_2)