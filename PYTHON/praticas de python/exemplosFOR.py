for i in range(7):
    print("Gol da Alemanha")
print("Gol do Brasil")



set_alunos = {'João', 'Neto', 'Maria', 'Amanda'}
for aluno in set_alunos:
    print(aluno)
    
#aluno com indice

alunos = ['João', 'Felipe', 'José', 'Antonio']
for aluno in enumerate(alunos):
    print(aluno)
    
#dicionario

alunos = {'João':5, 'Neto':8, 'Ana':20}
for chave in alunos:
    print(chave)
for chave in alunos.values():
    print(chave)
for aluno, nota in alunos.items():
    print(f'O(a) aluno(a) {aluno} tirou nota {nota} na prova.')