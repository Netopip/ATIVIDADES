from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'Neto': randint(1,6),
    'Victoria': randint(1,6),
    'Neta': randint(1,6),
    'Thomas': randint(1,6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado. ')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('== RANKING ==')
for i, v in enumerate(ranking):
    print(f' {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)

#quando ranking recebe sorted(colocar em ordem crescente), a lista é preenchida, na lista é dada por indice e valores, e se usa enumerate em listas, enquanto em dicionarios usa-se .items().O modulo operator e itemgetter faz com que a chave(key) seja escolhida dentro da lista(ou dicionario) com a evidencia entre parentese[] no caso o indice 1(que sao os valores de randint). E o reverse True signfica colocar na ordem inversa.