from numpy import *

custos = array(eval(input()), dtype=float)
i = 0
while(i < len(custos)):
	if(custos[i] > 80.0):
		custos[i] = custos[i]*0.85
	i += 1
print(round(sum(custos), 2))
