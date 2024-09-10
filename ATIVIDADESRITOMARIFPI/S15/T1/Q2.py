'''Considere uma tupla que guarde temperaturas em Celsius (C) ou Fahrenheit (F) como um valor em duas partes: temperatura e escala. Por exemplo: 32,5 graus Celsius é representado como (32.5, ‘C’) e 45,2 graus Fahrenheit é representado como (45.2, ‘F’). Desenvolva uma função que soma duas temperaturas que podem estar em Celsius ou em Fahrenheit. Se as duas temperaturas estiverem na mesma escala, a resposta deve estar na mesma escala. Se as temperaturas estiverem em escalas diferentes, a resposta deve ser dada na escala da segunda temperatura. Considere até 4 (quatro) casas decimais).'''

def calcular_temp(t1,escala1,t2,escala2):
    if escala1 == escala2:
        t = t1 + t2
        tupla = round(t,4),escala1
        return tupla
    
    elif escala1 == 'F' and escala2 == 'C':
        t1_c = (t1 - 32) * (5/9)
        t1_c = t1_c + t2 
        tupla = round(t1_c,4),escala2
        return tupla
    
    elif escala1 == 'C' and escala2 == 'F':
        t1_f = (t1 * (9/5)) + 32
        t1_f = t1_f + t2
        tupla = round(t1_f,4),escala2
        return tupla

def main():
    
    t1 = float(input().strip())
    escala1 = str(input()).strip().upper()
    t2 = float(input().strip())
    escala2 = str(input()).strip().upper()
        
    tupla = calcular_temp(t1,escala1,t2,escala2)
    print(tupla)
    
if __name__ == '__main__':
    main()
    