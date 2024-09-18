def q_digitos_pares(numero):
    contador = 0
    while numero > 0:
        digito = numero % 10
        if digito % 2 == 0:
            contador += 1
        numero //= 10
    return contador

def main():
    numero = int(input())
    
    if 100 <= numero <= 999:
        digitos_pares = q_digitos_pares(numero)
        print(digitos_pares)
    else:
        print(1)

if __name__ == "__main__":
    main()
