#valores = list(range(4,11))
#print(valores)

#valores = [8, 2, 5, 4, 9, 3, 0]
#valores.sort() coloca em ordem crescente
#print(valores.sort(reverse=True)) coloca a ordem em decrescente
#len(valores) a quantidade de elementos

#num = [2, 5, 9, 1]
#num[2]= 3
#num.append(7)
#num.sort(reverse=True)
#num.insert(2, 2)
#num.remove(2) #elimina so o primeiro 2
#if 4 in num:
#    num.remove(4)
#else:
#    print(f'Não achei o numero 4')
#num.pop(2)
#print(num)
#print(f'Essa lista tem {len(num)} elemento.')

#valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)

#for c,v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}!')
#print('Cheguei ao final da lista')

#valores = list()
#for cont in range(0, 5):
#    valores.append(int(input('Digite um valor:')))
#for c,v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}!')
#print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(a)
print(b)