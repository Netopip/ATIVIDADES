#import uteis - maneira mais recomendada.
from uteis import fatorial,dobro


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {dobro(num)}')
    
