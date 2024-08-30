def calcular_numero(data):
    soma = 0
    while data > 0:
        soma += data % 10
        data //= 10
    return soma

def main():
    data_nascimento = int(input())
    numero = calcular_numero(data_nascimento)
    print(numero)

if __name__ == '__main__':
    main()