def calcular_conjunto(lista):
    soma = sum(lista)
    return soma


def main():
    lista = list()
    while True:
        numero = int(input())
        if numero == 0:
            break
        if numero > 0:
            lista.append(numero)
        elif numero < 0:
            print()
            continue
    soma = calcular_conjunto(lista)
    print(soma)

if __name__ == '__main__':
    main()

