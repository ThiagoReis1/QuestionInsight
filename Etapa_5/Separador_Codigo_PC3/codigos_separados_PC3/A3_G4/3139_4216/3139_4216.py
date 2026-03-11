from numpy import *
v = array(eval(input("insira n: ")))
soma = 0
n = size(v)


for i in range(size(v)):
	soma = soma + v[i]**(1/3)
	d = n
eq = (soma/n)**3
				
print(round(eq, 2))