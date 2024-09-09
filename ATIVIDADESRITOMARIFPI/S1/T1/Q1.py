'''Escreva um algoritmo/programa que receba valor do preço de produto e o valor pago pelo cliente. Calcule e exiba o valor do troco a ser dado.'''

def main():
    valor = float(input())
    dinheiro = float(input())
    if dinheiro < valor:
        print(f'Pagamento Insuficiente')
    else:
        troco = dinheiro - valor
        print(f"{troco:.2f}")

if __name__ == '__main__':
    main()