def intercalar(lista, lista2):
    listac = []
    for a,b in zip(lista, lista2):#intercalar os numeros da lista com as da lista 2,é usada para agrupar elementos de duas ou mais listas (ou qualquer outro iterável) em pares, formando uma lista de tuplas onde cada tupla contém um elemento de cada uma das listas fornecidas.
        listac.append(a)
        listac.append(b)
    return listac


def main():
    n = 25
    lista = []
    for i in range(n):
        numero = int(input())
        lista.append(numero)
    print(lista)

    lista2 = []
    for j in range(n):
        numero1 = int(input())
        lista2.append(numero1)
    print(lista2)

    listac = intercalar(lista, lista2)
    print(listac)



if __name__ == '__main__':
    main()

