combo = input("Tipo de combo ").upper()
quantidade = int(input("Quantidade de combos: "))

d = 30.00 * quantidade
n = d - 0.15 * d

if (combo == "C"):
	print(round(n,2))
else:
	print(round(d,2))