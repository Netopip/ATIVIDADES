
num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais numero: ')),
       int(input('Digite o último numero: ')))
print(f'Voçê digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posição.') # o index retorna o indice do parametro
else:
    print(f'O valor 3 não foi digitado.')    
print(f'Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
