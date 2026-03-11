compra = float(input("Insira o valor total da compra: "))
codigo = input("Insira o codigo da compra: ").upper()

if (codigo == "D"):
	total = compra - (compra * 17/100)
elif (codigo == "P"):
	total = compra - (compra * 17/100)
elif (codigo == "C1"):
	total = compra
else:
	total = compra + (compra * 8/100)

print(round(total, 2))