'''Usando apenas as estruturas básicas de programação, reescreva a funções count(), que recebe uma lista e um valor e retorna o número de ocorrências do valor na lista. Por exemplo count([1, 2, 3, 2, 4, 2, 5], 2) retorna 3, a quantidade de vezes que o valor 2 aparece na lista.

Faça a leitura pelo teclado, a leitura de um 0 (zero) encerra a leitura. Primeiro leia a lista e depois o valor para pesquisar. Imprima a lista que foi lida, o valor pesquisado e o resultado encontrado.'''

def count(lista,valor):
    cont = 0
    for i in range(len(lista)):
        if lista[i] == valor:
            cont += 1
    return cont
        

def main():
    lista = []
    while True:
        numero = int(input())
        if numero == 0:
            break
        lista.append(numero)
    valor = int(input())
    
    cont = count(lista,valor)
    print(f'{lista}\n{valor}\n{cont}')
    
if __name__ == '__main__':
    main()