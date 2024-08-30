
deposito_inicial = float(input())
taxa_juros = float(input())
juros = (taxa_juros/100)

valor = deposito_inicial
anos = 0

while valor < 2 * deposito_inicial:
    valor += valor * juros
    anos += 1

print(anos)
