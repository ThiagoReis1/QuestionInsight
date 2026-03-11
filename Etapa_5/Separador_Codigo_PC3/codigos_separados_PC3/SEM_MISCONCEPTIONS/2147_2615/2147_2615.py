cpf = input()
cpf = str(cpf)

impar = 0

if ((len(cpf)) == 11):
	for i in range(len(cpf)):
		if (i % 2 != 0):
			impar = impar + 1
			
	saida = ""
		
	for a in range(len(cpf)):
		if (a % 2 != 0):
			saida = saida + cpf[a]
				
	print (saida)
	
else:
	print ("INVALIDO")