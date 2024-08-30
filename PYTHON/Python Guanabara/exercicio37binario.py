numero = int(input('Digite um numero inteiro:'))
print(''' Escolha uma das bases para conversao:
      [1] binario
      [2] octal
      [3] hexadecimal''')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print(numero, bin(numero))
elif opcao == 2:
    print(numero, oct(numero))
elif opcao == 3:
    print(numero, hex(numero))
else:
    print('opcao invalida')
