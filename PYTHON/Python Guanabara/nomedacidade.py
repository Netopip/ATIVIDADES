#cidade = str(input('Digite a sua cidade'))
#print((cidade[0:5]) == 'Santo')

cidade = str(input('Digite a sua cidade:')).strip()
print(cidade[:5].upper() == 'SANTO')