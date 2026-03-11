item = input("Tapioca ou Salgado: ")
quant = int(input("Quantidade: "))
acai = int(input("Quantidade de acai: "))

if (item ==  "T"):
	final = quant * 3.50 + acai * 13
	print(round(final, 2))
else:
	final = quant * 5 + acai * 13
	print(round(final, 2))