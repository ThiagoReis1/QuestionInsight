Pj = int(input("Digite um numero(x): "))

soma = Pj % 13
if soma == 0:
	print(Pj//13)
	print ("sim")
else:
	print(Pj%13)
	print ("nao")