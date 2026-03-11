prato = input("").upper()
quantidades = int(input(""))
qcafe = int(input(""))
if prato == "B":
	valor = (3.00 * quantidades) + (5.50 * qcafe)
	print(valor)
else:
	valor = (6.00 * quantidades) + (5.50 * qcafe)
	print(valor)