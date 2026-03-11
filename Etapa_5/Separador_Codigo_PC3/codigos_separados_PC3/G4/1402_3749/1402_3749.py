arma = input("nome da arma (machado/lanca) ")
fator = int(input("fator de sucesso: "))

x = 30 * fator / 10
y = 5 + 20 * fator / 10

if (arma == "machado"):
	print(int(x))
else:
	print(int(y))