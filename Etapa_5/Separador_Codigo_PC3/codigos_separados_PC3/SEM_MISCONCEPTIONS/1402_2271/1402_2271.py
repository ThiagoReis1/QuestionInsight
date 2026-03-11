arma = input("Nome da arma (machado/lanca): ")
fator = int(input("dado de dez faces (1/10): "))
if(arma == "machado"):
	print(30*fator/10)
else:
	print(5+20*fator/10)
