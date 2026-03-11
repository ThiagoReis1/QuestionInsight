compra = float(input("valor total da compra: "))
cod = input("codigo da compra: ")

if cod.upper() == "D" or cod.upper() == "P":
	total = compra - (compra * 17/100)
elif cod.upper() == "C1":
	total = compra
elif cod.upper() == "C2":
	total = compra + (compra * 8/100)
print(round(total, 2))