numero = int(input("Digite os numeros inteiros: "))
qtdeN = 0
qtdeP = 0

while numero != 0:
	qtdeN = qtdeN + 1
	if (numero>0):
		qtdeP = qtdeP + 1
	numero = int(input("Digite um numero: "))
	
print(qtdeN)
print(round(100*(qtdeP/qtdeN),2))
	