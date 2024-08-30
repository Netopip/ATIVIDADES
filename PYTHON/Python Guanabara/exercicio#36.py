casa = float(input())
salario = float(input())
ano = int(input())

prestaçao = casa / (ano * 12)
minimo = (salario * (30/100))
if prestaçao <= minimo:
    print('Emprestimo concedido.')
else:
    print('Emprestimo negado.')

print(f'Para uma casa no valor de {casa}, com o salario de {salario} a prestacao ficara {prestaçao:.2f}')

