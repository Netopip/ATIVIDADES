r1 = float(input())
r2 = float(input())
r3 = float(input())

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1+ r2:
    print('pode ser um triangulo.', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISOCELES!')    
else:
    print('Nao pode ser um triangulo.')