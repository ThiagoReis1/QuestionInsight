from numpy import *

vt = array(eval(input("Tempo dos banhos: ")))
vp = array(eval(input("Percentual de abertura da torneira: ")))

c = 0 
i = 0
consumo = 0

while (c < size(vt)):

	consumo = consumo + 0.05 * vp[i] * vt[i]	
	c = c + 1
	i = i + 1
	
print(round(consumo, 2))