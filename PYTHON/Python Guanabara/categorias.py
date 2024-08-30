from datetime import date
data_nascimento = int(input('Digite sua data de nascimento: '))
data_atual = date.today().year
idade = data_atual - data_nascimento
if idade <= 9:
    print('MIRIM')
elif idade <=14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('VELHO')
