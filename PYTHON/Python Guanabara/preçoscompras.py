preco_da_compra = float(input('Qual o valor da compra: '))
print(''' formas de pagamnetos
      [1] À vista
      [2] À vista cartao
      [3] 2x no cartao
      [4] 3x ou mais no cartao''')
opcao = int(input('Digute a sua opção: '))
if opcao == 1:
    total = preco_da_compra - (preco_da_compra * 10/100)
elif opcao == 2:
    total = preco_da_compra - (preco_da_compra * 5/100)
elif opcao == 3 :
    total = preco_da_compra 
    parcela = total / 2
    print(f'Sua compra sera parcelada em 2x de {parcela:.2f}')
elif opcao == 4:
    total = preco_da_compra + (preco_da_compra * 20/100)
    n_parcelas = int(input('Quantas parcelas? '))
    parcela = total / n_parcelas
    print(f'Sua compra sera parceladas em {n_parcelas:.2f} de {parcela:.2f}')
else:
    total = preco_da_compra
    print('Opcao invalida')
print(f'Sua compra de R$ {preco_da_compra:.2f} vai custar R$ {total:.2f}')


