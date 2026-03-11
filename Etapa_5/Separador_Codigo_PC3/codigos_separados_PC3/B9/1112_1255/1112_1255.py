salario = float(input("digite o salario:"))
print("Entrada: R$", salario)
	
if(salario < 0):
	print("Dado invalido")
else:
		if(salario <= 800):
			salario_total= round(salario + salario * 0.5, 2)
			print("Novo salario: R$",salario_total)
		elif((salario > 800)and(salario <= 1000)):
			salario_total= round(salario + salario * 0.4, 2)
			print("Novo salario: R$",salario_total)
		elif((salario > 1000)and(salario <= 1200)):
			salario_total= round(salario + salario * 0.3, 2)
			print("Novo salario:R$",salario_total)	
		elif((salario > 1200)and(salario <= 1400)):
			salario_total= round(salario + salario* 0.2, 2)
			print("Novo salario:R$",salario_total)
		elif((salario > 1400)and(salario <= 1600)):
			salario_total= round(salario + salario* 0.1, 2)
			print("Novo salario:R$",salario_total)
		elif(salario > 1600 ):
			salario_total= round(salario + salario* 0.05, 2)
			print("Novo salario:R$",salario_total)
		else:
			print("Dados invalidos")
	

	