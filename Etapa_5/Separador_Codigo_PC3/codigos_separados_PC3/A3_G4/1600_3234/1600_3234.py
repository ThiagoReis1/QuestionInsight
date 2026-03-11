from numpy import*
x=array(eval(input("digite o custo de cada item: ")))
p=0
i=0
cont=0
while (i<size(x)):
	if(x[i]>80):
		p=0.85*x[i]
	
	else:
		p=x[i]
	cont=cont+p	
	i=i+1
	
print(round(cont,2))