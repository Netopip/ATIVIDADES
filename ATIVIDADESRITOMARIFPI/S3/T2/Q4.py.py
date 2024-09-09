minutos = int(input())

horas = minutos //60
minutos_resto = minutos % 60

print(horas,"h",minutos_resto,"min", sep="")
