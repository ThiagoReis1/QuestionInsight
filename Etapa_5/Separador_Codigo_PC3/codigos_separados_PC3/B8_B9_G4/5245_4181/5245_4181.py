a = float(input("Salario atual: "))
print("Entrada: R$", a)

if (a > 0 ):
	if(a <= 800):
		y= a+ a/100*50
	elif(a<=1000):
		y = a + a/100*40
	elif(a <= 1200):
		y = a + a/100*30
	elif(a <= 1400):
		y = a + a/100*20
	elif(a <= 1600):
		y = a + a/100*10
	elif(a > 1600):
		y = (a + a/ 100 * 5)
	print("Novo salario: R$", round(y, 2))
else:
	print("Dado invalido")