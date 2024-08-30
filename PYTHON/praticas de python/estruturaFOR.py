# for - palavra reservada do python repetição com final determinado
# for each == "para cada" //
lista_produto = ["faca;", "garfo;", "panela;", "frigideira"]
for k in lista_produto : # o k é uma  variavel contadora
     print(k.capitalize())# o captalize coloca a primeira letra de cada item maiusculo

produtos ={      #dicionario
    "faca": 10,
    "garfo": 10,
    "panela": 200,
    "frigideira": 50,
}
for item in produtos:
    print(item)
    #dicionario[chave]
    print(produtos[item])

for i in range(5):# conjunto de numeros de 0 a 5 excluindo o 5º
    print(i+1)

for _ in range(2):#convenção pois voce é obrigado a colocar a variavel para funcionar.
    print("Amor da minha vida")


#exercicio do video:
#with open ("vendasloja.txt", "r") as arquivo:
#    texto = arquivo.read()
#print(texto.split("\n"))#.split separa todos os caracteres #abrir aqrivos dentro do python
#faturamento = 0
#lista_texto = lista_texto[1:]
#print(lista_texto)
#for linha in lista_texto:
#    posicao_pv = linha.find(";")
#    valor = float(linha[posicao_pv + 1: ])
#    faturamento += valor

for i in range(7):
    print("Gol da Alemanha")
print("Gol do Brasil")

# Estrutura de repetiçõa
# for elemento in lista:
set_alunos = ['ana', 'João']
for aluno in set_alunos:
    print(aluno)
