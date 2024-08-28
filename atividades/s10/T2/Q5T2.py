def main():
    valor = float(input())
    for i in range(1, 25):
        parcela = valor / i
        print(f'{i}x de R$ {parcela:.2f}')
if __name__ == '__main__':
    main()