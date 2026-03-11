bs = input("Informe B ou C: ")
quant = float(input("Informe a quantidade de comida: "))
capp = float(input("Informe a quantidade de cappuccinos: "))

if bs.upper() == "B":
	valor = quant * 3 + capp * 5.50
	print(round(valor, 1))
else:
	valor = quant * 6 + capp * 5.50
	print(round(valor, 1))