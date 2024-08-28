def main():
    deposito_inicial = float(input("Digite o valor do depósito inicial: R$ "))
    taxa_juros = float(input("Digite o valor da taxa de juros anual: "))
    juros = (taxa_juros/100)

    valor = deposito_inicial
    anos = 0

    while valor < 2 * deposito_inicial:
        valor += valor * juros
        anos += 1
    print(f'O total de anos necessários para que o valor do deposito inicial dobre é {anos} anos, com um total de R$ {valor:.2f}')

if __name__ == '__main__':
    main()
