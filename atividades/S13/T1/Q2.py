def main():
    lista = []
    n = int(input())
    for a in range(n):
        lista.append(0)
    print(lista)

    lista1 = list()
    for b in range(1, n+1):
        lista1.append(b)
    print(lista1)

    lista2 =[]
    for c in range(n):
        n1 = int(input())
        lista2.append(n1)
    print(lista2)

    lista3 = []
    for d in range(n):
        n2 = int(input())
        lista3.insert(0,n2)
    print(lista3)


if __name__ == '__main__':
    main()
