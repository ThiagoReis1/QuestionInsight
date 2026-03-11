from numpy import *
v = array(eval(input("custo dos itens: ")))
i = 0

while(i < size(v)):
	if(v[i] > 80):
		v[i] = v[i] * 75 / 100
	i = i + 1
print(round(sum(v), 2))