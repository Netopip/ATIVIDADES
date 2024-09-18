def celsius_para_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def main():

    temperatura_celsius = float(input())

    temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

    print(f'{temperatura_fahrenheit:.2f}')

if __name__ == "__main__":
    main()
