from numpy import *
cust=array(eval(input(" ")))
i=0
cont=0
while(i<size(cust)):
	if(cust[i]>90):
		desconto=cust[i]-6.50
		cont=cont+desconto
	else:
		cont=cont+cust[i]
	i=i+1
print(round(cont,2))