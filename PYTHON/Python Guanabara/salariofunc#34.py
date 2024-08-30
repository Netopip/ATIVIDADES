salario = float(input())
if salario <= 1250:
    novo_salario1 = (salario) + (salario * (15/100)) 
    print(novo_salario1)   
else:
    novo_salario2 = (salario) + (salario * (10/100))
    print(novo_salario2)