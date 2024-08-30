def calcular_lista(numeros):
    nova_lista = []
    for i in range(len(numeros)):
        if i % 2 == 0:
            nova_lista.append(numeros[i] * 3)
        else:
            nova_lista.append(numeros[i] * 5)
    return nova_lista


def main():
    numeros = []
    for i in range(100):
        n = int(input())
        numeros.append(n)
        numeros.sort()

    nova_lista = calcular_lista(numeros)
    print(nova_lista)

if __name__ == '__main__':
    main()