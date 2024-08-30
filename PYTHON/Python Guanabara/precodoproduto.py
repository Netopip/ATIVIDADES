def calcular_desconto(valor_produto):
    desconto = (valor_produto) - (valor_produto * 5 / 100)
    return desconto

def main():
    valor_produto = float(input('Digite o valor: R$'))

    valor_final = calcular_desconto(valor_produto)

    print(f'O valor do produto com desconto é R$ {valor_final}')
if __name__ == "__main__":
    main()