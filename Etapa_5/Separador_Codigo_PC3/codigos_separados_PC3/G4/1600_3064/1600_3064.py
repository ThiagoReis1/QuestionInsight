from numpy import*
x=array(eval(input("Informe o custo dos produtos: ")))
i=0
s=0
while (i< size(x)):
	if (x[i] > 80.0):
		s= s+(x[i]-(x[i]*0.15))
	else:
		s=s+x[i]
	i=i+1
print(round(s,2))	