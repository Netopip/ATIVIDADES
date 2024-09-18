def analisar_digitos(numero):
    digito1 = numero // 10
    digito2 = numero % 10

    if digito1 % 2 == 0 and digito2 % 2 == 0:
        print("Nenhum dígito é ímpar.")
    elif digito1 % 2 != 0 and digito2 % 2 != 0:
        print("Os dois dígitos são ímpares.")
    else:
        print("Apenas um dígito é ímpar.")

def main():
    numero = int(input())

    if 10 <= numero <= 99:
        analisar_digitos(numero)
    else:
        print()

if __name__ == "__main__":
    main()
