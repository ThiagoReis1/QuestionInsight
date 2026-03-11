atual = float(input("Digite o valor do salario atual: "))

if(atual < 0):
	print("Dado invalido")
	
elif((atual >=0)and (atual <= 800)):
	a = 0.5
	y= atual + (atual*a)
	print("Novo salario:", "R$", round(y,2))
	
elif((atual > 800) and (atual <= 1000)):
	a = 0.4
	y = atual + (atual*a)
	print("Novo salario:", "R$", round(y,2))
	
elif((atual > 1000) and (atual <= 1200)):
	a = 0.3
	y = atual + (atual*a)
	print("Novo salario:", "R$", round(y,2))
	
elif((atual > 1200) and (atual <= 1400)):
	a = 0.2
	y = atual + (atual*a)
	print("Novo salario:", "R$", round(y,2))
	
elif((atual > 1400) and (atual <= 1600)):
	a = 0.1
	y = atual + (atual*a)
	print("Novo salario: R$", round(y,2))
	
else:
	a = 0.05
	y = atual + (atual*a)
	print("Novo salario: R$", round(y,2))
	