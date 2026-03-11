from numpy import*
r= 8.95
d=array(eval(input("")))
i=0
cont=0
while(i<size(d)):
	if (d[i]>r):
		cont=cont+1
	i=i+1
print(r)
print(cont)