from datetime import date

atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento :'))
idade = atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')
if idade == 18:
    print(f'Voce tem que se alistar imediatamente.')
elif idade < 18:
    saldo = 18 - idade
    print(f'Voce ainda nao tem 18 anos anos, ainda falta {saldo} anos para o seu alsitamento. ')
    saldo = 18 - idade
elif idade > 18:
    saldo = idade - 18
    print(f'Voce ja deveria ter se alistado há {saldo} anos.')