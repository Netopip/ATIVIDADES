def analisar_nome(nome):
    nome_maisculo = nome.upper()
    nome_minusculo = nome.lower()
    letras = (len(nome)-nome.count(' ')) #nome menos o espaço.
    primeiro_nome = nome.split()[0]
    letras_primeiro_nome = nome.find(' ')
    return [nome_maisculo, nome_minusculo , letras, primeiro_nome, letras_primeiro_nome]





def main():
    nome = str(input('Digite seu nome completo:')).strip()

    analise = analisar_nome(nome)

    print(f'Seu nome maiusculo é {analise[0]},\n seu nome minusculo é {analise[1]},\n a quantidade de letras do seu nome é {analise[2]},\n seu primeiro nome é {analise[3]},\n a quantidade de letras do seu primeiro nome é {analise[4]}')

if __name__ == "__main__":
    main()