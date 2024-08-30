nome = str(input('Digite seu nome:'))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome =='Pedro' or nome == "Marcia" or nome == 'Paulo':
    print('Seu nome é bem popular no Brail')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}!')
