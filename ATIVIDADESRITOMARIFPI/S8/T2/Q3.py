'''Escreva um programa que leia um número inteiro positivo e escreva na tela:

• FIZZ se o número é divisível por três;

• BUZZ se o número é divisível por cinco;

• FIZZBUZZ se o número é divisível por três e por cinco ao mesmo tempo.

• O próprio número caso não seja divisível por três ou por cinco.

OBS: para cada número lido apenas uma resposta deve ser impressa.'''

def resposta(n):
    if n % 3 == 0 and n % 5 == 0:
        print('FIZZBUZZ')
    elif n % 3 == 0:
        print('FIZZ')
    elif n % 5 == 0:
        print('BUZZ')
    else:
        print(n)
        
        
def main():
    n = int(input())
    
    resposta(n)
    
if __name__=='__main__':
    main()