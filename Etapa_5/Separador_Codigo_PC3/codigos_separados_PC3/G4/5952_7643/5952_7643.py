item = input("Tapioca ou Salgado (T/S): ").upper()
quantidade = int(input("Quantidade: "))
acai = int(input("Quantidade de acai: "))

if item == "T":
	a = (quantidade * 3.50) + (acai * 13)
	print(round(a,2))
else:
	v = (quantidade * 5.00) + (acai * 13)
	print(round(v,2))