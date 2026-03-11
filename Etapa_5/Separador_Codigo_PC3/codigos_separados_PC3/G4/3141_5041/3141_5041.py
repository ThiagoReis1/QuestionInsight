from numpy import *

v = array(eval(input("Digite numeros positivos: ")))

i = 0
p = 0

if v[i]>0:
	while (i)<size(v):
		p = p + v[i]**(1/6)
		i = i + 1
	M = (p/(size(v)))**6
print(round(M, 2))