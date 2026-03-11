numero = int(input("digite numero inteiro: "))
i = 0
while (numero != 0):
	
	if (numero > 0):
		msg = "POSITIVO"
	if(numero < 0):
		msg = "NEGATIVO"
	i = i + 1
	print (msg)
	numero = int(input("digite numero inteiro: "))
	
