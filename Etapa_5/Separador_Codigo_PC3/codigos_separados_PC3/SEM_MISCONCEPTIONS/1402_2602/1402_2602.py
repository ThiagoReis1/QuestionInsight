arma = input("Digite o nome da arma: ")
fator = int(input("Digite o fator de sucesso: "))
if (arma =="machado".lower()): 
	D = 30 * fator/10 
	print (int(D))
else: 
	D = 5 + 20* fator/10
	print (int(D))