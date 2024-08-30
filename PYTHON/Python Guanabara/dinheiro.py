def calcular_dolar(dinheiro):
    valor = dinheiro / 3.27
    return valor

def main():
    dinheiro = float(input('Quanto reais voce tem? R$'))

    total = calcular_dolar(dinheiro)

    print(f'Voçe consegue comparar {total:.2f} dólares!')

if __name__ == "__main__":
    main()
