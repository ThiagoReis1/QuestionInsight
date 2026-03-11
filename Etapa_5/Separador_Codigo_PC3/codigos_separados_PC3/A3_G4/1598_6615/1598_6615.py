from numpy import *
V =array(eval(input("precos: ")))
d = 6.50
i = 0
while(i<size(V)):
	if(V[i]>90):
		V[i]= V[i]-6.50
	else:
		V[i]==V[i]
	i = i +1
print(round(sum(V),2))