arma = input("Nome da arma: ")
fator = int(input("Fator de sucesso: "))

if (arma == "machado") and (fator >= 1) and (fator <=10):
	dano = 30*fator/10
	print(int(dano))
if (arma == "lanca") and (fator >= 1) and (fator <=10):
	dano = 5+20*(fator/10)
	print(int(dano))
