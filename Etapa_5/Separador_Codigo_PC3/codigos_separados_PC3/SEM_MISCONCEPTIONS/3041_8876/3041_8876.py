x = float(input("Numero: "))

if -1000 <= x and x < -2:
	funcao = -(1/(x + 2))
	print(round(funcao, 4))
elif 2 < x and x <= 1000:
	funcao = 1/(x - 2)
	print(round(funcao, 4))
else:
	print("entrada invalida")
	