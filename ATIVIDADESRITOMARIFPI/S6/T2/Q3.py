def main():
   
    preco_maca = float(input())
    preco_banana = float(input())

    quantidade_macas = 3
    quantidade_bananas = 2

    total_compra = (preco_maca * quantidade_macas) + (preco_banana * quantidade_bananas)

    print(f'{total_compra:.2f}')

if __name__ == "__main__":
    main()
