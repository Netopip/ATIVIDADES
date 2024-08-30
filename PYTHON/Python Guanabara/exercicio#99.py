from time import sleep


def maior(*num):
    cont = maior = 0
    print('-='*20)
    print(f'\nAnalisando os valores passados...') #\n quebra a linha.
    for valor in num:
        print(f'{valor} ', end='', flush=True) #o flush tira o erro de nao mostrar a contagem na tela!
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 5, 5 ,8)
maior(2, 3, 8, 4)
maior(6)
maior()