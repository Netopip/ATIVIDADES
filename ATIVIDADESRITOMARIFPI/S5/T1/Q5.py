def inverter_numero(numero):
    numero_invertido = str(numero)[::-1]
    return numero_invertido

def main():
    numero = int(input())

    if 1000 <= numero <= 9999:
        numero_invertido = inverter_numero(numero)
        print(numero_invertido)

    else:
        print()

if __name__ == "__main__":
    main()
