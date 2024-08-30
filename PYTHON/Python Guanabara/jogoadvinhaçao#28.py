from random import randint

computador = randint(0,5)
print('--=--' * 20)
print('Vou pensar em um numero entre 0 e 5, tente advinhar...')
print('--=--' * 20)

jogador = int(input('Em que numero eu pensei:'))
if jogador == computador:
    print('PARABENS! voce consegui me vencer')
else:
    print(f'GANHEI! Eu pensei no numero {computador}')