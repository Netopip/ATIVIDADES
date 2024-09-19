'''Fazer um programa para ler uma matriz n x m de números inteiros. Os valores de n e m são inteiros, positivos e devem ser informados pelo usuário, calcular e armazenar em uma tupla para mostrar, respectivamente: a) a soma dos elementos da primeira linha b) a soma dos elementos da última coluna c) a média de todos os elementos d) o menor elemento e) o maior elemento

'''

def definir_matriz(n,m):
    matriz = []
    
    for i in range(n):
        linha = []
        for j in range(m):
            numero = int(input().strip())
            linha.append(numero)
        matriz.append(linha)
    
    return matriz

def soma_1_liha(matriz):
    soma = 0
    for i in matriz[0]:
        soma += i
    return soma

def soma_ultima_coluna(matriz):
    soma_coluna = 0
    for l in matriz:
        soma_coluna += l[-1]
    return soma_coluna

def media_dos_elementos(matriz):
    soma = 0
    elementos = 0
    for linha in matriz:
        soma += sum(linha)
        elementos += len(linha)
    media = soma / elementos
    return round(media,4)

def menor_elemento(matriz):
    menor = matriz[0][0]
    for linha in matriz:
        menor_linha = min(linha)
        if menor_linha < menor:
            menor = menor_linha
    return menor

def maior_elemento(matriz):
    maior = matriz[0][0]
    for linha in matriz:
        maior_linha = max(linha)
        if maior_linha > maior:
            maior = maior_linha
    return maior
 

def main():
    n = int(input().strip())
    m = int(input().strip())
    
    matriz = definir_matriz(n,m)
    soma = soma_1_liha(matriz)
    soma_coluna = soma_ultima_coluna(matriz)
    media = media_dos_elementos(matriz)
    menor = menor_elemento(matriz)
    maior = maior_elemento(matriz)  
    print(f'({soma}, {soma_coluna}, {media}, {menor}, {maior})')
    
if __name__ == '__main__':
    main()