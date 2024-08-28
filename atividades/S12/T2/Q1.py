def calcular_fatorial(n):
    if n < 0:
        return
    elif n == 0 or n == 1:
        return 1
    else:
        farotial = 1
        for i in range(2, n+1):
            farotial *= i
        return farotial


def main():
    numero = int(input())

    resultado = calcular_fatorial(numero)
    print(resultado)

if __name__ == '__main__':
    main()