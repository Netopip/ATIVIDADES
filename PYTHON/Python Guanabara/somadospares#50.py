soma = 0
cont = 0

for n in range(1, 7):
    num = int(input(f'Digite o valor {n}:'))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
    
print(f'Voce informouo {cont} numeros pares, e a soma foi {soma}.')