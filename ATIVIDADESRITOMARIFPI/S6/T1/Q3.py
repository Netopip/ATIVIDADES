def main():
    tempo_segundos = int(input())

    horas = tempo_segundos // 3600
    minutos = (tempo_segundos % 3600) // 60
    segundos = tempo_segundos % 60

    tempo_format = '{:02d}:{:02d}:{:02d}'.format(horas, minutos, segundos)

    print(tempo_format)

if __name__ == "__main__":
    main()
