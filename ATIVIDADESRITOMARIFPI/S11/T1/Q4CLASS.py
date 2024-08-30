def numero_invertido(numero):
    inverso = str(numero)[::-1]
    inteiro = int(inverso)
    return inteiro

def main():
    valor = int(input('Digite um numero inteiro: '))
    numero = numero_invertido(valor)
    print(f'O numero {valor} invertido é {numero}.')

if __name__ == '__main__':
    main()