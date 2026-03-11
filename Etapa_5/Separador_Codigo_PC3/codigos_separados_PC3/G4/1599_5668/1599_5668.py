from numpy import *
ci = array(eval(input("custo dos itens: ")))
i = 0
while i < size(ci):
	if(ci[i] > 80):
		ci[i] = ci[i] - (ci[i] * (15/100)) 
	i+=1
	ct = sum(ci)
print(round(ct, 2))