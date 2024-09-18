def calcular(a, b, c):
    return 2 * a + 5 * b - c

def main():
    a = int(input())
    b = int(input())
    c = int(input())

    resultado_equacao = calcular(a ,b ,c)
    print(resultado_equacao)

if __name__ == "__main__":
    main()
