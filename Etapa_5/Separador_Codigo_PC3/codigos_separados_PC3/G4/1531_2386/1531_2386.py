from math import *
#Angulo
x = eval(input())
#Numero Inteiro
k = int(input())
#denominador/expoente
di = 2
i = 1
exp = 2
soma = 1.0

while(di < k):
	soma = soma + (-1**i)*(x**exp)/factorial(exp)
	exp = exp+2
	di = di + 1
	i = i + 1

X = round(soma, 10)
print(X)

