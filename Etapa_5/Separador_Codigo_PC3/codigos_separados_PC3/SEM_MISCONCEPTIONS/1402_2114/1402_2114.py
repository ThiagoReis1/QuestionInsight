arma = input("digite a arma: ")
fator = int(input("digite o valor do fator de sucesso: "))

if(arma == "machado"):
	print(int(30*(fator/10)))

if(arma == "lanca"):
	print(int(5+(20*(fator/10))))