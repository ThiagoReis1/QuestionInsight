from math import*
x =  float(input("Numero real X: "))
k =  int(input("Nuemro inteiro K:")) + 2
soma = 0 
cont = 0 
while(cont<=k):
	f = ((((1) ** cont)) * (x ** (2 + cont + 1))/(factorial(2 * cont + 1)))
	soma = soma + f
	cont = cont + 1
print(round(soma,9))
