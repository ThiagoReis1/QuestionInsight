# Phillip de sousa
# 18/07/2016
# Av 3, Ex 01

X = float(input("Digite o lado X: ")) 

print("Entrada:","R$",X)

if(X < 0):
	print("Dado invalido")
elif(0 <= X <= 800):
	X = X + 0.50*X
	print("Novo salario: R$",round(X,2))
elif(800 < X <= 1000 ):
	X = X + 0.40*X
	print("Novo salario: R$",round(X,2))
elif(1000 < X <= 1200 ):
	X = X + 0.30*X
	print("Novo salario: R$",round(X,2))
elif(1200 < X <= 1400):
	X = X + 0.20*X
	print("Novo salario: R$",round(X,2))
elif(1400 < X <= 1600):
	X = X + 0.10*X
	print("Novo salario: R$",round(X,2))
elif(1600 < X):
	X = X + 0.05*X
	print("Novo salario: R$",round(X,2))