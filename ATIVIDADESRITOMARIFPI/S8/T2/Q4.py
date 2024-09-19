'''Escreva um programa que leia a altura e o sexo de uma pessoa, considere 1 para 'homens' e 2 para 'mulheres'. Usando duas casas decimais, calcule e mostre o peso ideal utilizando as seguintes fórmulas:

• para homens: (72.7 * altura) – 58

• para mulheres: (62.1 * altura) – 44.7'''

def peso_ideal(altura,sexo):
    if sexo == 1:
        peso = (72.7 * altura) - 58
    elif sexo == 2:
        peso = (62.1 * altura) - 44.7 
    return peso


def main():
    altura = float(input())
    sexo = int(input())
    
    peso = peso_ideal(altura,sexo)
    print(f'{peso:.2f}')
    
if __name__ == '__main__':
    main()