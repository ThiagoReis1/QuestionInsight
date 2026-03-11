x= float(input("salario atual: "))

if(x>=0):
	if(x<=800.00):
		y= x + (x*50/100)
		print("Entrada: R$",round(x,2))
		print("Novo salario: R$", round(y,2))
	elif(x>800.00 and x<=1000.00):
		y= x + (x*40/100)
		print("Entrada: R$", round(x,2))
		print("Novo salario: R$", round(y,2))
	elif(x>1000.00 and x<=1200.00):
		y= x + (x* 30/100)
		print("Entrada: R$", round(x,2))
		print("Novo salario: R$", round(y,2))
	elif(x>1200.00 and x<=1400.00):
		y= x + (x*20/100)
		print("Entrada: R$", round(x,2))
		print("Novo salario: R$", round(y,2))
	elif(x>1400.00 and x<=1600.00):
		y= x + (x*10/100)
		print("Entrada: R$", round(x,2))
		print("Novo salario: R$", round(y,2))
	elif(x>1600.00):
		y= x + (x*5/100)
		print("Entrada: R$", round(x,2))
		print("Novo salario: R$", round(y,2))

else:
	print("Entrada: R$", round(x,2))
	print("Dado invalido")