sa=float(input("Salario atual: "))

if(sa>0 and sa<800.00):
	var=round(sa+(sa*0.50),2)
	print("Novo salario: R$",var)
elif(sa>800.00 and sa<1000.00):
	var=round(sa+(sa*0.40),2)
	print("Novo salario: R$:",var)
	
elif(sa>1000.00 and sa<1200.00):
	var=round(sa+(sa*0.30),2)
	print("Novo salario: R$",var)

elif(sa>1200.00 and sa<1400.00):
	var=round(sa+(sa*0.20),2)
	print("Novo salario: R$",var)
	
elif(sa>1400.00 and sa<1600.00):
	var=round(sa+(sa*0.10),2)
	print("Novo salario: R$",var)

elif(sa>1600.00):
	var=round(sa+(sa*0.05),2)
	print("Novo salario: R$",var)

else:
	print("Dado invalido")