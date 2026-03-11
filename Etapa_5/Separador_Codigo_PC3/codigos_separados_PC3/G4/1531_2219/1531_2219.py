from math import*

angx = eval(input("Informe o angulo medido em radianos:"))
k = int(input("Informe o número de termos K:"))

soma = 0
cont = 1

while(cont < k):
	soma =soma + (((angx**(cont*2))/(factorial(cont*2)))*((-1)**cont))
	cont = cont +1
	
print(round(1 + soma,10))

