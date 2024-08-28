numero = int(input())
cont = 0

for i in range(1,numero + 1):
    if numero % i == 0:
        cont += 1
if cont == 2:
    print(True)
else:
    print(False)