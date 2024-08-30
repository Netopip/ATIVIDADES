def main():
    while True:
        print('OPÇÕES:\n'
              '1 - SAUDAÇÃO\n'
              '2 - BRONCA\n'
              '3 - FELICITAÇÃO\n'
              '0 - FIM ')
        opcao = int(input())
        if opcao == 1 :
            print('Olá. Como vai?')
        elif opcao == 2:
            print('Vamos estudar mais.')
        elif opcao == 3:
            print('Meus Parabéns!')
        elif opcao == 0:
            print('Fim de serviço.')
            break
        else:
            print('Opção inválida.')
if __name__ == '__main__':
    main()