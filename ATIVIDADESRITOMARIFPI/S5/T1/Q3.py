def calculo_acrescimo(preco, percentual):
    return preco * (1 + percentual/100)
def calculo_desconto(preco, percentual):
    return preco * (1 - percentual/100)

def main():
    preco =float(input())
    percentual =float(input())

    preco_aumento = calculo_acrescimo(preco, percentual)
    preco_desconto = calculo_desconto(preco, percentual)

    print(f"{preco_aumento:.2f}")
    print(f"{preco_desconto:.2f}")

if __name__ == "__main__":
    main()
