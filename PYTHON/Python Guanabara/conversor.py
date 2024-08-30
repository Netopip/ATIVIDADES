def conversao_temp(temperatura):
    temp = ((9*temperatura)/5)+32
    return temp


def main():
    temp = float(input('Digite a temperatura em °C:'))

    conversao = conversao_temp(temp)

    print(f'A temperatura de {temp}°C para F é { conversao}')

if __name__ == "__main__":
    main()
