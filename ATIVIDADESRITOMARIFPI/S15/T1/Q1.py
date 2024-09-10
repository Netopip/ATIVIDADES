'''01. Considereuma tupla que guarde temperaturas em Celsius (C) ou Fahrenheit (F) como um valor em duas partes:
temperatura e escala. Por exemplo: 32,5 graus Celsius é representado como (32.5, ‘C’) e 45,2 graus Fahrenheit é
representado como (45.2, ‘F’). Crie uma função que recebe duas temperaturas e retorna a mais alta. Caso as
temperaturas sejam de escalas diferentes, a função deve fazer a conversão antes de compará-las. Faça a leitura de
duas temperaturas, na forma temperatura e escala (t, e) separadamente, e mostre qual é a maior. Considere até 4
(quatro) casas decimais).
Use upper() e colchetes [] para garantir a leitura correta da escala com apenas um caractere, por exemplo:
escala = input('Escala : ').upper()[0]
As fórmulas, a seguir, mostram como realizar a conversão entre as escalas solicitadas::
°F = (°C * (9/5)) + 32 | °C = (°F - 32) * (5/9)'''

def conversao(t1,escala1,t2,escala2):
    if escala1 == escala2:
        tupla1 = (t1,escala1)
        tupla2 = (t2,escala2)
        return tupla1 if tupla1 > tupla2 else tupla2
    
    elif escala1 == 'F' and escala2 == 'C':
        t1_c = (t1 - 32) * (5/9)
        tupla1 = (t1,escala1)
        tupla2 = (t2,escala2)
        return tupla1 if t1_c > t2 else tupla2
    
    elif escala1 == 'C' and escala2 == 'F':
        t2_c = (t2 -32) * (5/9)
        tupla1 = (t1,escala1)
        tupla2 = (t2,escala2)
        return tupla1 if t1 > t2_c else tupla2
        
  
def main():
    t1 = float(input())
    escala1 = str(input()).strip().upper()[0]
    t2 = float(input())
    escala2 = str(input()).strip().upper()[0]
    
    resultado = conversao(t1,escala1,t2,escala2)
    print(resultado)
    
if __name__ == '__main__':
    main()
    
    