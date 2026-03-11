comida = input("B ou S:")
Qts = int(input("quantidade de tapioca ou salgado: "))
Qacai = int(input("quantidade de acai: "))

if comida == "S":
	valor = (Qts*5.00) + (Qacai*12.00)
	print(round(valor, 2))
	
else:
	valor = (Qts*4.50) + (Qacai*12.00)
	print(round(valor, 2))