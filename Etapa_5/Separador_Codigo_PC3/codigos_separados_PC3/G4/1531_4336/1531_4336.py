from math import*
x = eval(input("Medida do angulo em radianos: "))
termos = int(input("Quantidade de termos: "))
cos = 1
cont = 1

if (termos == 1):
	cos
else:
	while cont < termos:
		cos = cos - (x ** 2) / factorial(cont*2)
		cont = cont + 1
		
print(cos)
