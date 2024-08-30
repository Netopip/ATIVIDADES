def calcular_hipotenusa(adjacente, oposto):
    hipotenusa = ((adjacente ** 2) + (oposto ** 2)) ** (1/2)
    return hipotenusa


def main():
    adjacente = float(input('Digite o valor do cateto adjacente:'))
    oposto = float(input('Digite o valor do cateto oposto:'))

    total = calcular_hipotenusa(adjacente, oposto)

    print(f'O valor da hipotenusa é {total:.2f}')

if __name__ == "__main__":
    main()

