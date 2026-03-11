from numpy import * 
vc = array(eval(input("")))
i = 0
custo = 0 

while i < size(vc) :
	if vc[i] > 90 :
		vc[i] = vc[i] - 6.5 
	i = i + 1
custo = sum(vc) 
print(round(custo,2))