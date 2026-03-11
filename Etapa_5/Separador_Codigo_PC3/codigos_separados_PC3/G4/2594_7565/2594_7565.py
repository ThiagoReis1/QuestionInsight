from numpy import*
d=array(eval(input(": ")))
cont=0
for i in range(1,size(d)):
	if(d[0]<d[i]):
		print(i)
		cont = cont+1
print(cont)