'''Escreva um algoritmo/programa que receba o valor do quilo de um produto e a quantidade de quilos consumida desse produto. Calcule e exiba o valor final a ser pago.'''
def calcular_total(valor, quant):
    total = valor * quant
    return total

def main():
    valor = float(input())
    quant = float(input())
    
    total = calcular_total(valor,quant)
    print(f'{total:.2f}')
    
if __name__ == '__main__':
    main()
    
    