'''Faça um programa que leia duas listas de 10 elementos. Crie uma lista que seja a união entre as 2 listas anteriores, ou seja, que contêm os números das duas listas. Não deve conter números repetidos.'''

def unir_lista(lista_1, lista_2):
    nova_lista = []
    for i in lista_1:
        if i not in nova_lista:
            nova_lista.append(i)
    for i in lista_2:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista
    
def main():
    lista_1 = []
    lista_2 = []
    for i in range(10):
        numeros1 = int(input())
        lista_1.append(numeros1)
    for i in range(10):
        numeros2 = int(input())
        lista_2.append(numeros2)
    
    nova_lista = unir_lista(lista_1, lista_2)
    print(nova_lista)
        
if __name__=='__main__':
    main()
        
    
    