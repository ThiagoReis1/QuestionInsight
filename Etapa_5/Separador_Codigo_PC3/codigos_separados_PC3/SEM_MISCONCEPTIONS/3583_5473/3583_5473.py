from numpy import *

custo = array(eval(input("custo dos itens: ")))

i = 0 
total = 0

while(i<size(custo)):
	if(custo[i]>50):
		total = total + (custo[i] - (custo[i]*0.08))
	else:
		total = total + custo [i]
	
	i = i + 1
	
print(round(total,2))
