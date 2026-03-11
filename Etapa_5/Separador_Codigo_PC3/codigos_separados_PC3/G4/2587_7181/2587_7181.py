from numpy import*

v=array(eval(input(" ")))
i=0
cont=0
m=v[0]+(v[0]*0.5)
while(i<size(v)-1):
	if(m<v[i+1]):
		print(i+1)
		cont=cont+1
	i=i+1

print(cont)