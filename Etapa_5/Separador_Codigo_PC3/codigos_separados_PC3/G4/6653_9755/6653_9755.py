from numpy import *

#vetorP = [3, 5, 1]

v = array(eval(input("digite sua nota: ")))

i = 0

while i <= 0:
	a = v[0]*3
	b = v[1]*5
	c = v[2]*1
	
	soma = a+b+c
	total = soma/9
	i = i+1
	
print(round(total, 2))