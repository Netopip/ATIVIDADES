

primeiro = int(input('Primeiro termo:'))
razao = int(input('Razao:'))
decimo = primeiro + (10 - 1) * razao
for n in range(primeiro, decimo + razao, razao):
    print(f'{n}', end='-')
print('acabou')