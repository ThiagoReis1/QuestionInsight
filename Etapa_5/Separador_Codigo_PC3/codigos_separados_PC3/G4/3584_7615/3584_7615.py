from numpy import *
v= array(eval(input("digite o vetor de custo: ")))

a= 0
i= 0
while i < size(v):
	if v[i] >= 200:
		a= a + (v[i] - (v[i] * 0.15))
	else:
		a= a + v[i]
	i+=1
	
print(round(a,2))