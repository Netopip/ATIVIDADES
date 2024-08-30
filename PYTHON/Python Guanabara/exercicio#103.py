def cadastro( jogador ='desconhecido', gols = 0):# O parametro com igualdade é um parametro opcional, como jogador que se não tiver parametro para substitui-lo receberá 'desconhecido'.
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')
      
    
nome = str(input('Qual o nome do jogador: '))
gol = str(input('Quantos gols ele fez: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    cadastro(gols=gol)
else:
    cadastro(nome, gol)
