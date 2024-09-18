def calcular_valores_compra(valor_compra):
    valor_vista = valor_compra * 0.91

    valor_prazo_5x = valor_compra / 5

    valor_prazo_10x = (valor_compra * 1.17) / 10

    return valor_vista, valor_prazo_5x, valor_prazo_10x

def main():
    valor_compra = float(input())

    valor_vista, valor_prazo_5x, valor_prazo_10x = calcular_valores_compra(valor_compra)

    print(valor_vista)
    print(valor_prazo_5x)
    print(valor_prazo_10x)

if __name__ == "__main__":
    main()
