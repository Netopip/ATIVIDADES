from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''
      [0]pedra
      [1]papel
      [2]tesoura''')
jogador = int(input('Digite a sua jogada:'))

print(f'O computador jogou {itens[computador]}.')
print(f'O jogador jogou {itens[jogador]}.')

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHA')
        
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')


