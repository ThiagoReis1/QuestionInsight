kws = float(input("quantidade consumida: "))

preco = (kws * 0.43) + 10
valor = preco + preco * (25/100)

print(round(valor, 2))