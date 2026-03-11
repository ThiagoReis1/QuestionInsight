preco = float(input("Digite valor do produto sem desconto:"))
taxa_do_desconto = 40

valor_do_frete = preco * (5 / 100)
preco_com_desconto = (preco - (preco * (taxa_do_desconto / 100)))

print(round(preco_com_desconto, 2))
print(round(valor_do_frete, 2))