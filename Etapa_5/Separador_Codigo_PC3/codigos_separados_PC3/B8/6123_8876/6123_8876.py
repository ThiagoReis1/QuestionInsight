fuel = float(input("Quantidade de combustivel: "))

if fuel < 17.5:
	mistura = fuel + 0.8
	print(round(mistura, 1))
elif 17.5 < fuel < 35:
	mistura = fuel + 1.3
	print(round(mistura, 1))
elif 35 < fuel < 50:
	mistura = fuel + 2.1
	print(round(mistura, 1))
elif fuel > 50:
	mistura = fuel + 3
	print(round(mistura, 1))