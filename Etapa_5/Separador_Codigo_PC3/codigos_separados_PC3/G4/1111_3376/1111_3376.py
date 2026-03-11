x = float(input("horas extras: "))
y = float(input("horas faltadas: "))
h = x - (2/3)*y
if h > 2400:
	g = 500.0
	print("Entradas:", round(x,2), "horas extras e", y, "horas de falta")
	print("Gratificacao: R$", g)
elif h > 1800 and h < 2400:
	g = 400.0
	print("Entradas:", round(x,2), "horas extras e", y, "horas de falta")
	print("Gratificacao: R$", g)
elif h > 1200 and h < 1800:
	g = 300.0
	print("Entradas:", round(x,2), "horas extras e", y, "horas de falta")
	print("Gratificacao: R$", g)
elif h > 600 and h < 1200:
	g = 200.0
	print("Entradas:", round(x,2), "horas extras e", y, "horas de falta")
	print("Gratificacao: R$", g)
elif h < 1600:
	g = 100.0
	print("Entradas:", round(x,2), "horas extras e", y, "horas de falta")
	print("Gratificacao: R$", g)
else:
	print("Entradas:", round(x,2), "horas extras e", y, "horas de falta")
	print("Dados invalidos")



