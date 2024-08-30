

qualquer = str(input('Digite um numero ou letra: '))
#print(qualquer.isalpha())
#print(qualquer.isalnum())
#print(qualquer.isnumeric())
if qualquer.isnumeric():
    qualquer = int(qualquer)
print(qualquer + 5)
