def converter_minutos(minutos):
    horas = minutos // 60
    minutos_rest = minutos % 60
    return horas, minutos_rest

def main():
    minutos = int(input())

    horas,minutos_rest = converter_minutos(minutos)

    print(horas,":", minutos_rest, sep='')
   
if __name__ == "__main__":
    main()
     
