#def teste():
#    x = 8 #varialvel local(escopo local), so tem valor dentro da função def
#    print(f'Na função teste, n vale {n}')
#    print(f'Na função teste, x vale {x}')
    
#programa principal
#n = 2 #Escopo global, funciona em todo o programa.
#print(f'No programa principal, n vale {n}')
#teste()
#print(f'No programa principal, x vale {x}')

def funcao():
    n1 = 4
    print(f'n1 dentro vale {n1}')
    
n1 = 2
funcao()
print(f'n1 fora vale {n1}')
print('-=' *30)
def teste(b):
    global a 
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')