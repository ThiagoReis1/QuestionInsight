arma = input("Nome da arma:")
fator = int(input("valor do dado entre 1 e 10:"))

machado = (30 * fator/10)
lanca = (5 + 20 * fator/10)

if (arma == "machado"):
	dano = machado
else:
	dano = lanca
print(int(dano))

