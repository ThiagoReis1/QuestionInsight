from math import *
x = eval(input("um angulo: "))
y = int(input("quantidade de termos da serie: "))

soma = 1
i = 1


while(i < y):
	soma = soma + ((-1)**i * (x**(2*i))/factorial(2*i))
	i = i + 1

print(round(soma, 10))