from numpy import*

v=array(eval(input(" ")))
i=0
cont=0
while(i<size(v)-1):
	if(v[i+1]<v[0]):
		print(i+1)
		cont=cont+1
	i=i+1
	
print(cont)	