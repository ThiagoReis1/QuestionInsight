arma = input("Machado ou lanca")
fator = int(input("Digite um valor entre 1 e 10: "))

machado = 30 * fator/10
lanca = 5 + 20 * fator/10

if(arma == "machado"):
	print(machado)
else:
	print(lanca)