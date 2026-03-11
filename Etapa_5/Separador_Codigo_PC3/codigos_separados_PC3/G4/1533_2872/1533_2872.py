from math import*
x = float(input("Digite um numero: "))
k = int(input("Informe o numero de termos: "))
i = 1
soma = 0
while (i<k):
	termo = (x**(2*i))/(factorial(2*i))
	soma = soma + termo
	i = i+1
print(round(1+soma,8))