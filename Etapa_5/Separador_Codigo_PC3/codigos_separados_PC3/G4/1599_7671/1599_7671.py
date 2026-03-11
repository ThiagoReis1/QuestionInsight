#Desconto
from numpy import *


comp = array(eval(input("compras: ")))

i = 0 
desc = 0

while(i<size(comp)):
	if(comp[i] > 80.0):
		desc = desc + comp[i] * 15/100
	i = i + 1

total = sum(comp) - desc
print(round(total,2))
	