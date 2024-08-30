def main():
    poupanca = 10000
    rendimento_poupanca = 0.007
    taxa_carro = 0.004
    valor_carro = float(input())
    tempo_meses = 0
    while valor_carro > poupanca:
        poupanca = poupanca + (poupanca * rendimento_poupanca)
        valor_carro = valor_carro + (valor_carro * taxa_carro)
        tempo_meses +=1
    print(tempo_meses)

if __name__ == '__main__':
    main()

