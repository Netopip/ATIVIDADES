'''O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso ideal. O IMC é determinado pela divisão da massa do indivíduo pelo quadrado de sua altura, em que a massa está em quilogramas e a altura em metros. Escreva um programa que leia a massa (o peso) e a altura de uma pessoa e calcula o IMC de uma pessoa, e depois, mostra uma das seguintes mensagens:

IMC	Classificação
< 18,5	Abaixo do peso
< 25	Peso normal
< 30	Sobrepeso
< 35	Obeso leve
< 40	Obeso moderado
>=40	Obeso mórbido'''
def calcular_imc(peso,altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print (f'{imc}\nAbaixo do peso')
    elif imc < 25:
        print (f'{imc}\nPeso normal')
    elif imc < 30 :
        print (f'{imc}\nSobrepeso')
    elif imc < 35 :
        print (f'{imc}\nObeso leve')
    elif imc < 40:
        print (f'{imc}\nObeso moderado')
    elif imc >= 40:
        print (f'{imc}\nObeso mórbido')
    return imc
def main():
    
    peso = float(input())
    altura = float(input())
    
    calcular_imc(peso,altura)
    
if __name__ == '__main__':
    main()