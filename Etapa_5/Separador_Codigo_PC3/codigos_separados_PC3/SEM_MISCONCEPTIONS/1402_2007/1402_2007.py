arma = input("digite nome da arma: ")
fator = int(input("digite um numero: "))
if (arma == "lanca"):
	dano = 5 + (20 * fator/10)
else:
	dano = 30 * (fator/10)
print (dano)
