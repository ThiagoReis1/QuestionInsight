x = float(input("Informe o valor do salario: "))
print("Entrada: ", "R$",x)
if(x > 0 and x <= 800):
	y = x + (x * 0.50)
	print("Novo salario: ","R$",round(y,2))
elif(x > 800 and x <= 1000):
	y = x + (x * 0.40)
	print("Novo salario: ","R$",round(y,2))
elif(x > 1000 and x <= 1200):
	y = x + (x * 0.30)
	print("Novo salario: ","R$",round(y,2))
elif(x > 1200 and x <= 1400):
	y = x + (x * 0.20)
	print("Novo salario: ","R$",round(y,2))
elif(x > 1400 and x <= 1600):
	y = x + (x * 0.10)
	print("Novo salario: ","R$",round(y,2))
elif(x > 1600):
	y = x + (x * 0.05)
	print("Novo salario: ","R$",round(y,2))
else:
	print("Dado invalido")
