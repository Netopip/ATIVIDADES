from random import randint
from time import sleep
lista = list()
jogos = list()
quantidade = int(input('Quantos jogos de loteira você quer: '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'Os numeros sorteados foram {jogos}')
for i , l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('< Boa Sorte! >')