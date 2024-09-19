'''Faça um programa que receba a temperatura média de cada mês do ano. A temperatura pode ser informada em graus Celsius, Fahrenheit ou Kelvin. Após isto, calcule a média anual das temperaturas e mostre, em Kelvin, todas as temperaturas acima da média anual e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, ... ).'''

def converter_temp(temp):
    temperaturas_convertidas = []
    for i in  temp:
        if i[1] == 'C':
            i[0] = i[0] +273.15
            i[1] = 'K'
            temperaturas_convertidas.append(tuple([i[0],i[1]]))
        elif i[1] == 'F':
            i[0] = ((i[0] -32)/1.8) + 273.15
            i[1] = 'K'
            temperaturas_convertidas.append(tuple([i[0],i[1]]))
        else:
          if i[1] == 'K':
              temperaturas_convertidas.append(tuple([i[0],i[1]]))
            
    return temperaturas_convertidas

def media_temp(temperaturas_convertidas):
    soma = 0
    cont = 0
    for i in temperaturas_convertidas:
        soma += i[0]
        cont += 1
    media = soma / cont
    return round(media,2)

def temperaturas_acima_media(media,temperaturas_convertidas):
    mes = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
    for i,temp in enumerate(temperaturas_convertidas):
        if temp[0] > media:
            print(f'{mes[i]}: {round(temp[0],2)}K')
            
        

def main():
    temp = []
    
    for i in range(12):
        temperatura = float(input().strip())
        escala = str(input()).upper().strip()
        temp.append([temperatura,escala])
        
    temperaturas_convertidas = converter_temp(temp)
    media= media_temp(temperaturas_convertidas)
    
    print('TEMPERATURA MÉDIA ANUAL')
    print(f'{media}K')
    
    print('TEMPERATURAS ACIMA DA MÉDIA ANUAL:')
    temperaturas_acima_media(media,temperaturas_convertidas)
    
        
        
if __name__ == '__main__':
    main()