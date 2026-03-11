sal = float(input("salario: "))

if (sal >0):
	if (sal > 0) and (sal <= 800):
		a =  ((sal*50)/100)
		total = sal + a
		print("Novo salario: R$",round(total,2))
	elif (sal > 800) and (sal <= 1000):
		b = ((sal*40)/100)
		total2= sal + b
		print("Novo salario: R$",round(total2,2))
	elif (sal > 1000) and (sal <= 1200):
		c = ((sal*30)/100)
		total3= sal + c
		print("Novo salario: R$", round(total3,2))
	elif (sal > 1200) and (sal <= 1400):
		d = ((sal*20)/100)
		total4 = sal + d
		print("Novo salario: R$", round(total4,2))
	elif (sal > 1400) and(sal <= 1600):
		e = ((sal*10)/100)
		total5= sal + e
		print("Novo salario: R$", round(total5,2))
	elif (sal > 1600):
		f = ((sal*5)/100)
		total6= sal + f
		print("Novo salario: R$", round(total6,2))
else:
	print("Dado invalido")