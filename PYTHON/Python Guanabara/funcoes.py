#def soma(a, b):
#    print(f'A={a} e B={b}')
 #   s = a + b
 #   print(f'A soma de A + B = {s}')
    
#soma(5, 4)
#soma(8, 9)
#soma(2, 1)
#-------------------------------------------------------------
#def contador(*num): (# o asterisco é uma desempacotar, nao sabe quantos são os parametros )
#    tam = len(num)
#    for valor in num:
#        print(f'{valor} ', end='')
#    print(f'Recebi os valores {num} e são {tam} números. ')
#    print('FIM')

#contador(2, 1, 7)
#contador(6, 0)
#contador(4, 5, 9, 7)
#------------------------------------------------------------

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
        
    
valores =[7,2,5,6,3]
dobra(valores)
print(valores)
