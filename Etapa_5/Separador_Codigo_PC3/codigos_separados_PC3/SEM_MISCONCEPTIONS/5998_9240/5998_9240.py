macas = int(input("macas: "))
valor_1 = (macas * 0.25)
valor_2 = (macas * 0.30)

if macas >= 12:
	print(round(valor_1, 2))
else:
	print(round(valor_2, 2))