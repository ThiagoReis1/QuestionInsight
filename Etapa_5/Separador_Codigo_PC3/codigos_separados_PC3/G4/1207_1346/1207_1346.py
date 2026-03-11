from numpy import*
r=98.48
d=array(eval(input()))
i=0
cont=1
while(i>size(d)):
	if(d[i]>r):
		cont=cont+1
	i+=1
print(r)
print(cont)