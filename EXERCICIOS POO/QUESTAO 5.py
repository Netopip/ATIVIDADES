'''QUESTAO PROPRIA DE UM TIME DE FUTEBOL
ADICIONAR E REMOVER JOGADOR DO CLUBE E EXIBIR OS
ATRIBUTOS DO JOGADOR'''

class Time:
    def __init__(self,nome_time):
        self.nome_time = nome_time
        self.jogadores = []

    def adicionar_jogador(self,jogador):
        self.jogadores.append(jogador)
        return f'Jogador {jogador.nome} contratado com sucesso para o {self.nome_time}!'

    def removerjogador(self,nome_jogador):
        for jogador in self.jogadores:
            if jogador.nome == nome_jogador:
                self.jogadores.remove(jogador)
                return f'Jogador {nome_jogador} não faz mais parte do {self.nome_time}.'
        return f'Jogador {nome_jogador} não encontrado ou já removido!'

    def listarjogadores(self):
        listar_jogadores = '\n'.join([jogador.exibirdetalhes() + f'\nTime:{self.nome_time}\n' for jogador in self.jogadores])
        return listar_jogadores

class Jogador:
    def __init__(self,nome,idade,nacionalidade):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade

    def exibirdetalhes(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nNacionalidade: {self.nacionalidade}'

flamengo = Time('Flamengo')
neto = Jogador('Neto' ,25 ,'BR')
jonas = Jogador('Jonas' ,25 ,'BR')
vini = Jogador('Vini' ,25 ,'BR')
victor = Jogador('Victor' ,22 ,'AR')


print(flamengo.adicionar_jogador(vini))
print(flamengo.adicionar_jogador(jonas))
print(flamengo.adicionar_jogador(neto))
print(flamengo.removerjogador('Neto'))


corinthians = Time('Corinthians')
print(corinthians.adicionar_jogador(neto))
print(corinthians.adicionar_jogador(victor))
print()
print(flamengo.listarjogadores())
print(corinthians.listarjogadores())


