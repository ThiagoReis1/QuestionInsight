salario=float(input("Digite o salario: R$"))

if (salario>0) and (salario<=800):
	print("Novo salario: R$ ",round(salario + (salario*0.5),2))
elif (salario>800) and (salario<=1000):
	print ("Novo salario: R$",round(salario + (salario*0.4),2))
elif (salario>1000) and (salario<=1200):
	print ("Novo salario: R$", round(salario + (salario*0.3),2))
elif (salario>1200) and (salario<=1400):
	print ("Novo salario: R$",round(salario + (salario*0.2),2))
elif (salario>1400) and (salario<=1600):
	print ("Novo salario: R$", round(salario + (salario*0.1),2))
elif (salario>1600):
	print("Novo salario: R$", round(salario + (salario*0.05),2))
else: 
	print("Dado invalido")