preco = float(input())

desconto = preco * 0.1
preco_com_desconto = preco - desconto
preco_com_desconto_arredondado = round(preco_com_desconto, 2)

print(f"{preco_com_desconto_arredondado:.2f}")
