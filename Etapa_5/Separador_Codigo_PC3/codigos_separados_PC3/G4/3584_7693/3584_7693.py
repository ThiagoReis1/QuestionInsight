from numpy import *

p = array(eval(input("digite o valor de cada compra: ")))

s = sum(p)
i = 0
cont = 0
while i < size(p):
	if p[i] > 200:
		cont = cont + p[i]*0.15
	i = i+1
	
print(round(s-cont,2))
