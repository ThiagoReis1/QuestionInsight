preco = float(input())
taxa_de_desconto = 40
frete = (preco * (5 / 100))
preco_com_desconto = preco - (preco * (taxa_de_desconto / 100))
print(round(preco_com_desconto, 2))
preco_final = (preco_com_desconto + frete)
print(round(frete, 2))