def calcular_area(lado):
    return lado * lado

def calcular_perimetro(lado):
    return 4 * lado

def main():
    lado = float(input())

    area = calcular_area(lado)
    perimetro = calcular_perimetro(lado)

    print("{:.4f}".format(area))
    print("{:.4f}".format(perimetro))

if __name__ == "__main__":
    main()
