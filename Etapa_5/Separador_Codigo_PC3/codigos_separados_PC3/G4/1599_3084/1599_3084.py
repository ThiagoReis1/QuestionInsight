from numpy import *
v = array(eval(input("Custo dos itens: ")))
i = 0 
d = 15/100
while(i<size(v)):
	if(v[i]>80):
		v[i] = v[i] - v[i]*d
		i = i + 1
	else:
		i = i + 1
print(round(sum(v),2))