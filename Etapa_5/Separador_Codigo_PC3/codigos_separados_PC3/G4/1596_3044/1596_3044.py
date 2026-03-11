from numpy import*
x=array(eval(input("notas: ")))
i=0
while(i<size(x)):
	if(i==min(x)):
		z=size(x)-i
	i=i+1
m=sum(x)-min(x)/z
print(round(m,2))

