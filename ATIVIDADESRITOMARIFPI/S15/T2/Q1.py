'''01.Faça um programa para ler uma matriz quadrada de ordem n e mostre uma tupla com a posição (linha e coluna) do
maior e menor elemento. O valore de n é inteiro, positivo e deve ser informados pelo usuário.'''

def maior_menor(matriz):
    menor = maior = matriz[0][0]
    pos_maior = (0,0)
    pos_menor = (0,0)
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                pos_maior = (i,j)
            if matriz[i][j] < menor:
                menor = matriz[i][j]
                pos_menor = (i,j)
    
    return pos_maior, pos_menor
            


def main():
   
    n = int(input())
    matriz = []
    
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(int(input()))
        matriz.append(linha)
        
    pos_maior, pos_menor = maior_menor(matriz)
    print(f'{pos_maior}\n{pos_menor}')
    
if __name__=='__main__':
    main()
    
    