a = int(input('Valor 1:'))
b = int(input('Valor 2:'))
c = int(input('valor 3:'))

#if a<b and a<c:
   # menor = a
#if b<c and b<a:
   # menor = b
#if c<a and c<b:
   # menor = c

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f'O mair valor digitado é {maior} ,e o menor valor é {menor}.')