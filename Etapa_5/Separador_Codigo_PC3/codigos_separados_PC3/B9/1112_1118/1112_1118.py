x = float(input())

print("Entrada: R$", x)
if x < 0:
	print("Dado invalido")
else:
	if x <= 800:
		total = x + 0.5*x
	elif x > 800 and x <= 1000:
		total = x + 0.4*x
	elif x > 1000 and x <= 1200:
		total = x + 0.3*x
	elif x > 1200 and x <= 1400:
		total = x + 0.2*x
	elif x > 1400 and x <= 1600:
		total = x + 0.1*x
	else:
		total = x + 0.05*x
	
	print("Novo salario: R$", round(total, 2))