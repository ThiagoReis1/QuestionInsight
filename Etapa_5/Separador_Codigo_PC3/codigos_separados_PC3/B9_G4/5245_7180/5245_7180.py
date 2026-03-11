salario = float(input("Salario atual: "))

print("Entrada: R$", salario)

if (salario>0): 
	if (salario <= 800):
		a = salario + (salario*0.50)
		print("Novo salario: R$", round(a,2))
	elif(salario>800) and (salario<=1000):
		b = salario + (salario*0.40)
		print("Novo salario: R$", round(b,2))
	elif(salario>1200) and (salario<=1200):
		c = salario + (salario * 0.30)
		print("Novo salario: R$", round(c,2))
	elif(salario>120) and (salario<=1400):
		d = salario + (salario * 0.20)
		print("Novo salario: R$", round(d,2))
	elif(salario>1400) and (salario<=1600):
		e = salario + (salario * 0.10)
		print("Novo salario: R$", round(e,2))
	elif(salario>1600):
		f = salario + (salario * 0.05)
		print("Novo salario: R$", round(f,2))
	else:
		print("Dado invalido")
else:
	print("Dado invalido")