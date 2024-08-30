
cont = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
        'onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito',
        'dezenove','vinte')
while True:
    numero = int(input('Digte um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('tente novamente! ', end='')
print(f'Voce digitou o número {cont[numero]}')
        

