from numpy import*

compras=array(eval(input()))
x=size(compras)
tot=0
for i in range(x):
	if(compras[i]>80.0):
		tot=tot+compras[i]-5
	else:
		tot=tot+compras[i]
		
print(round(tot,2))