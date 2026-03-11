from numpy import *

custoItems = array(eval(input()))
custoTotal = 0
i = 0

while(i < size(custoItems)):
	if(custoItems[i] > 160):
		custoTotal += custoItems[i] - 25
	else:
		custoTotal += custoItems[i]
	i += 1
	
print(round(custoTotal, 2))