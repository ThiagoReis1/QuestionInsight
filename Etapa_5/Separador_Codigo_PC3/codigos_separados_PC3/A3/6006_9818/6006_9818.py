batata = 0.90
compra = int(input("insira batatas compradas: "))

if compra >= 10:
	batata = 0.75
else:
	batata = 0.90

total = compra * batata

print(round(total, 2))