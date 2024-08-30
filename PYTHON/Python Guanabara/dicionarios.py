pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':'22'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.values():
    print(k)
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = '98.5'
for k ,v in pessoas.items():
    print(f'{k} = {v}')
