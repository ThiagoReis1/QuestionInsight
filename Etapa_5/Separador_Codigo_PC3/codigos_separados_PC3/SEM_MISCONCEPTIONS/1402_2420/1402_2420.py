arma = input("nome da arma: ")
ft = int(input("fator de sucesso: "))
machado = 30 * ft / 10
lanca = 5 + 20 * ft / 10
if(arma == "machado"):
	print(machado)
else:
	print(lanca)