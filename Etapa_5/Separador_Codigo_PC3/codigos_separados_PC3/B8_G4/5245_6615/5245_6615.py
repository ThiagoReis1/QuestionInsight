X = float(input("digite o salario atual de um funcionario: "))
print(("Entrada: R$"), X)
if(X<0):
	print("Dado invalido")
else:
	if(0<=X and X<=800.0):
		print("Novo salario: R$", round((X*0.5 + X),2))
	if(800.0<X and X<=1000.0):
		print("Novo salario: R$", round((X*0.4+X),2))
	elif(1000.0<X and X<=1200.0):
		print("Novo salario: R$", round((X*0.3+X),2))
	elif(1200.0<X and X<=1400.0):
		print("Novo salario:R$",round((X*0.2+X),2))
	elif(1400.0<X and X<=1600.0):
		print("Novo salario: R$", round((X*0.1+X),2))
	elif(1600.0<X):
		print("Novo salario: R$", round((X*0.05+X),2))
