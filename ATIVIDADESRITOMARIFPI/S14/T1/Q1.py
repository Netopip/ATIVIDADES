'''As estruturas básicas de programação são sequência, condição e repetição. Usando apenas as estruturas básicas de programação, reescreva as funções abaixo (sem utilizá-las):

a) len(), que recebe uma lista e retorna número de itens; b) reverse(), que recebe uma lista e retorna uma lista com os itens na ordem invertida; c) min(),que recebe uma lista e retorna o menor valor d) max(), que recebe uma lista retorna o maior valor e) sum(), que recebe uma lista retorna a soma dos valores

Faça a leitura dos valores necessários pelo teclado, a leitura de um número 0 (zero) encerra a leitura dos elementos da lista. Para cada uma das opções, imprima a lista que foi lida e o resultado encontrado.

Dica: Você pode usar esses nomes para suas funções: comprimento(), inverter(), minimo(), maximo(), soma().'''

def comprimento(lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont

def inverter(lista):
    nova_lista = lista[::-1]
    return nova_lista

def minimo(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i 
    return menor

def maximo(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior

def somar(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma
    
def main():
    lista = []
    while True:
        numero = int(input())
        if numero == 0:
            break
        lista.append(numero)
    cont, nova_lista, menor, maior, soma = comprimento(lista), inverter(lista), minimo(lista), maximo(lista),somar(lista)
    print(f'{lista}\n{cont}\n{nova_lista}\n{menor}\n{maior}\n{soma}')
    
if __name__ == '__main__':
    main()
        