x= float(input("Entrada:"))
print("Entrada: R$", x)
if(x>0):
	if(x<=800):	
		n= x + (x*0.50)
		print("Novo salario: R$",round(n,2))
	elif(x>800 and x<=1000.00):
		n= x + (x*0.40)
		print("Novo salario: R$",round(n,2))
	elif(x>1000.00 and x<=1200.00):
		n= x + (x*0.30)
		print("Novo salario: R$",round(n,2))
	elif(x>1200.00 and x<=1400.00):
		n= x + (x*0.20)
		print("Novo salario: R$",round(n,2))
	elif(x>1400.00 and x<=1600.00):
		n= x + (x*0.10)
		print("Novo salario: R$",round(n,2))
	elif(x>1600.00):
		n= x + (x*0.05)
		print("Novo salario: R$",round(n,2))
else:
	print("Dado invalido")