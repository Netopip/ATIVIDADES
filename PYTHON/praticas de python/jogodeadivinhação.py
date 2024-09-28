from random import randint

def main():
    print('Tente adivinhar o número do computador!')
    
    while True:
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
        
if __name__ == '__main__':
    main()
        

