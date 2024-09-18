def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if n3 > 8:
        media += 1
    if media > 10:
         media = 10
    return media

def main():
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())


    media_total = calcular_media(n1, n2, n3)

    print(media_total)

if __name__ == "__main__":
    main()
    
