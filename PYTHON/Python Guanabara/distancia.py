def calcular_centimetros(metros):
    cm = metros * 100
    return cm

def calcular_milimetros(metros):
    mm = metros * 1000
    return mm

def main():

    metros = float(input('digite o valor em metors:'))

    centimetros = calcular_centimetros(metros)
    milimetros = calcular_milimetros(metros)

    print(f'O valor de {metros}m corresponde à {centimetros}cm')
    print(f'O valor de {metros}m corresponde à {milimetros}mm')

if __name__ == "__main__":
    main()