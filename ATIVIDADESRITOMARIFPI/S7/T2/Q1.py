def contar_caracteres(nome1, estado_civil, nome2=None):
    total_caracteres = len(nome1)
    if estado_civil == 1:
        total_caracteres += len(nome2)
    return total_caracteres

def main():
    nome = input().strip()
    estado_civil = int(input().strip())

    if estado_civil == 1:
        nome_conjuge = input().strip()
        caracteres_totais = contar_caracteres(nome, estado_civil, nome_conjuge)
    else:
        caracteres_totais = contar_caracteres(nome, estado_civil)

    print(caracteres_totais)

if __name__ == "__main__":
    main()
