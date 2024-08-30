peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em M: '))

imc = peso / (altura ** 2)

print(f'O imc dessa pessoa é de {imc:.2f}.')

if imc < 18.5:
    print('Voce esta abaixo de peso normal.')
elif 18.5 <= imc < 25:
    print('Voce esta no peso ideal.')
elif 25 <= imc < 30 :
    print('Voce esta em sobrepeso.')
elif 30<= imc <40:
    print('Voce esta em obesidade')
else:
    print('Voce esta em obesidade morbida')

