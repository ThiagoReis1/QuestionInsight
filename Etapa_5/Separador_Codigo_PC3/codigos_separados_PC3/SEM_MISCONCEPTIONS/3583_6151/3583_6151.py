from numpy import *
comp= array(eval(input('digite a lista de compras feitas: ')))
i= 0
total= 0

while(i<size(comp)):
	if (comp[i]<=50):
		total= total+comp[i]
		i= i+1
	else: 
		total= total+(comp[i]-comp[i]*0.08)
		i= i+1

print(round(total, 2))