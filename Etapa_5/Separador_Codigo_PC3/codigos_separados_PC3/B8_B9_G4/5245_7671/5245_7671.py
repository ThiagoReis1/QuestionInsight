#Exercicio do salario do proletario

sa = float(input("Qual o salario atual? "))

p1 = sa * 50 / 100

p2 = sa * 40 / 100

p3 = sa * 30 / 100

if( sa > 0):
	if(sa <= 800.0):
		ns = sa + p1
		print("Novo salario: R$", round(ns,2))
	elif((sa > 800.0) and (sa <= 1000.0)):
		ns = sa + p2
		print("Novo salario: R$", round(ns,2))
	elif((sa > 1000.0) and (sa <= 1200.0)):
		ns = sa + p3
		print("Novo salario: R$", round(ns,2))
	elif((sa > 1200.0) and (sa <= 1400.0)):
		ns = sa + (sa * 20 / 100)
		print("Novo salario: R$", round(ns,2))
	elif((sa > 1400) and (sa <= 1600.0)):
		ns = sa + (sa * 10 / 100)
		print("Novo salario: R$", round(ns,2))
	elif(sa > 1600):
		ns = sa + (sa * 5 / 100)
		print("Novo salario: R$", round(ns,2))
else:
	print("Dado invalido")