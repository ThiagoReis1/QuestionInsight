from numpy import*
v = array(eval(input("Informe os pesos: ")))
x= 307
i= 0
c= 0
while(i<size(v)):
	if(v[i]>x):
		c=c+1
	i=i+1
print(x)
print(c)
	