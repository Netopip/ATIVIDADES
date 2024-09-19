def ler_data():
    dia = int(input())
    mes = int(input())
    ano = int(input())
    return dia, mes, ano

def data_maior(data1, data2):
    dia1, mes1, ano1 = data1
    dia2, mes2, ano2 = data2

    if ano1 > ano2:
        return data1
    elif ano1 < ano2:
        return data2
    else:  # anos são iguais
        if mes1 > mes2:
            return data1
        elif mes1 < mes2:
            return data2
        else:  # meses são iguais
            if dia1 > dia2:
                return data1
            else:
                return data2

data1 = ler_data()
data2 = ler_data()

data_recente = data_maior(data1, data2)

print(f"{data_recente[0]}/{data_recente[1]}/{data_recente[2]}")