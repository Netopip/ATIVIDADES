

#n = cont = 0 #programa le 5 numeros!
#while cont < 5:
#    n = int(input('Digite um numero: '))
#    cont += 1

#n = 0
#while n != 999:
#    n = int(input('Digite um numero: '))


n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')