#validando entrada de dados em Pytohn
#declaração da função leiaInt
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m') #codigo da cor vermelho
        if ok:
            break
    return valor


#programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')