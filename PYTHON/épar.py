
    
def eh_par(numero):
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é Ímpar')
        
def main():
    
    while True:
        entrada = str(input('Digite um número:\n'))
        try:
            number = int(entrada)
            eh_par(number)
        except ValueError:
            print('Entrada inválida!')
            continue    
        
        
        while True:
            opcao = str(input('Quer continuar: (SIM/NÃO)\n')).upper().strip()
            if opcao == 'NÃO':
                print(f'FIM DO PROGRAMA !')
                return
            elif opcao == 'SIM':
                break
            
            else:
                print('Opção inválida!')
            
        

if __name__ == '__main__':
    main()
    
                
            