num = int(input('Digite um numero:'))
total = 0
for n in range(1, num + 1):
    if num % n == 0:
        print('\033[33m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print(f'{n}', end=' ')
print(f'\n O numero {num} foi divisivel {total} vezes')
if total == 2:
    print('Esse é um numero primo!')
else:
    print('Esse não é um numero primo!')
    