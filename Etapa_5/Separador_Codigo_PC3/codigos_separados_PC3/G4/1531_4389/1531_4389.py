from math import*
x = eval(input("angulo: \n"))
k = int(input("Informe o numero de termos: \n"))
#x = eval(input("Informe o angulo: \n"))
cont = 0
soma = 0
i = 0

while(i<k):
	soma = soma + ((-1)**cont) * ((x**i)/factorial(i))
	cont = cont + 1
	i = i + 2
print(round(soma,10))
	