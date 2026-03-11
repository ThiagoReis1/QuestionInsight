X = int(input("valor de X: "))
Y = int(input("valor de Y: "))
cont = X
soma = 0

while(cont >= X) and (cont <= Y):
	if(cont % 2 == 0):
		cont = cont + 1
	else:
		soma = soma + cont
		cont = cont + 1
print(soma)