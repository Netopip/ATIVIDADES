


#while not apple:
 #  if chao:
  #      passo
   # if vazio:
    #    pule
    #if moeda:
     #   pega
#pega

#quando eu nao sei o limite.
#c = 1
#while c < 10:
#    print(c)
#    c = c + 1
#print('Fim')

#r = 'S'
#while r == 'S':
#    n = int(input('Digite um valor:'))
#    r = str(input('Quer continuar? [S/N]')).upper()
#print('Fim')

n = 1 
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 ==0:
            par = par + 1
        else:
            impar = impar + 1
print(f'Voce digitou {par} numeros pares, e {impar} numeros impares.')
