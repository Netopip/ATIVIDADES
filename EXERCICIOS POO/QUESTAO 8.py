class Aluno:
    def __init__(self,nome,idade='Não definida'):
        self.nome = nome
        self.idade = int(idade)


    def exibir_detalhes(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}'

class Curso:
    def __init__(self,nome_curso,tempo_curso):
        self.nome_curso = nome_curso
        self.duracao = tempo_curso
        self.alunos = []

    def adicionar_aluno(self,aluno):
        self.alunos.append(aluno)
        return f'Aluno {aluno.nome} adicionado ao curso de {self.nome_curso}'

    def remover_aluno(self,nome_aluno):
        for aluno in self.alunos:
            if aluno.nome == nome_aluno:
                self.alunos.remove(aluno)
                return f'Aluno {nome_aluno} removido com sucesso!'
        return f'Aluno {nome_aluno} não encontrado'

    def listar_aluno(self):
        lista_alunos = f'\n'.join([aluno.exibir_detalhes() + f'\nCurso: {self.nome_curso}\n' for aluno in self.alunos])
        '''lista=""
        for aluno in self.alunos:
            lista+= aluno.exibir_detalhes()
            lista+=f"\nCurso: {self.nome_curso}\n"'''
        return lista_alunos

neto = Aluno('Francisco', 25)
jonas = Aluno('Jonas', 25)
cinara = Aluno('Cynara', 23)
vini = Aluno('Vinicius',24)
vitorio = Aluno('Vitório',22)
flauta = Curso('Flauta',5)
clariente = Curso('Clarinete',5)
violao = Curso('Violão', 3)

print(flauta.adicionar_aluno(neto))
print(flauta.adicionar_aluno(jonas))
print(clariente.adicionar_aluno(cinara))
print(violao.adicionar_aluno(vini))
print(violao.adicionar_aluno(vitorio))
print()

print(flauta.listar_aluno())
print(clariente.listar_aluno())
print(violao.listar_aluno())