ficha = list()
while True:
    nome= str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+ n2)/2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
    
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando!')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
  