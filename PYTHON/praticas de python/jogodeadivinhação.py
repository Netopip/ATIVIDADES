from random import randint

def main():
    cont = 0
    print('Tente adivinhar o número do computador!')
    print('Você só tem 3 tentativas!')
    
    while cont < 3:
        numero_computador = randint(0,5)
        
        try:
            entrada = input('Digite o seu número entre 0 e 5:\n').strip()
            numero_jogador = int(entrada)
            
            if numero_jogador < 0 or numero_jogador > 5:
                print('Por favor, digite um número entre 0 e 5.')
                continue
        
        except ValueError:
            print('Entrada inválida!Por favor, insira um numero inteiro.')
            continue
        
        print(f'O númeor do computador é: {numero_computador}\nO seu número é: {numero_jogador}.')
        
        if numero_computador == numero_jogador:
            print('Parabéns, você ganhou!')
            break
        else:
            print('Você perdeu! Tente novamente!')
            cont += 1
    
    print()
    print('FIM DE JOGO')
        
if __name__ == '__main__':
    main()
        

