frase = 'Curso em Video Python'
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(len(frase)) #mostra quantos caracteres há na string contando com os espaços.
print(frase.count('o')) #mostra quantos 'o' tem na frase.
print(frase.count('o',0,13))# mostra a contagem da letra 'o' no fatiamento do 0 ao 12.
print(frase.find('deo'))#encontrar e mostra onde começa.
print(frase.find('Android'))
print('Curso' in frase)#operador para analise se existe 'Curso' na frase, no caso retorna True ou False.