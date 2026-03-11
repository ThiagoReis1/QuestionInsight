comida = input("digite:").upper()
qnt_comida = float(input("digite:"))
qnt_refri = float(input("digite:"))

Lanche = 6.00
Prato = 13.50
Refri = 3.00

if comida == "L":
	total = Lanche * qnt_comida + Refri * qnt_refri
	print(round(total))
	
else:
	comida == "P"
	total2 = Prato * qnt_comida + Refri * qnt_refri
	print(total2)