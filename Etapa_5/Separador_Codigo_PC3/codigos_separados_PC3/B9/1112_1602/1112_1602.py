salario=float(input("qual seu salario ?:"))
print("Entrada: R$",salario)
if (salario>0):
	if(salario<800):
		total=salario/2
		valor=total+salario
		print("Novo salario: R$",(round(valor,2)))
	elif(salario>=800 and salario<1000):
		total=salario*0.4
		valor=total+salario
		print("Novo salario: R$",(round(valor,2)))
	elif(salario>=1000 and salario<1200):
		total=salario*0.3
		valor=total+salario
		print("Novo salario: R$",(round(valor,2)))
	elif(salario>=1200 and salario<1400):
		total=salario*0.2
		valor=total+salario
		print("Novo salario: R$",(round(valor,2)))
	elif(salario>=1400 and salario<1600):
		total=salario*0.1
		valor=total+salario
		print("Novo salario: R$",(round(valor,2)))
	else:
		total=salario*0.05
		valor=total+salario
		print("Novo salario: R$",(round (valor,2)))
else:
	print("Dado invalido")