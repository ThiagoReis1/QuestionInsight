from math import*
a = eval(input("qual angulo vc escolhe?"))
k = int(input("qual quantidade de termos na serie?"))

i = 1 
soma = 0
fim = k
e = 2
while(i < fim):
	soma = soma + ((-1)**i) * ((a**e)/factorial(e))
	i = i+1
	e = e+2
soma = soma + 1
print(round(soma,10))