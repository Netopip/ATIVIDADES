def numero_invertido(numero):
    inverso = str(numero)[::-1]
    inteiro = int(inverso)
    return inteiro

def main():
    valor = int(input())
    numero = numero_invertido(valor)
    print(numero)

if __name__ == '__main__':
    main()