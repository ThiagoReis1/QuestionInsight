from numpy import *
v=array(eval(input("registros:")))
cont=0
i=1
for i in range(size(v)):
	if i!=0:
		if v[i]>=v[0]:
			print(i)
			cont=cont+1
print(cont)