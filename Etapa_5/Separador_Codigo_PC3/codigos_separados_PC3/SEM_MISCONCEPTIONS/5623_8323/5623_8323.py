lanche = input("Bolo (B) ou salgado (S)? ")
qnt = int(input("Quantidade: "))
cap = int(input("Quantidade de cappuccinos: "))

if (lanche == "B"):
	total = (5 * qnt) + cap * 7.50
	print(round(total, 2))
if (lanche == "S"):
	total = (4 * qnt) + cap * 7.50
	print(round(total, 2))