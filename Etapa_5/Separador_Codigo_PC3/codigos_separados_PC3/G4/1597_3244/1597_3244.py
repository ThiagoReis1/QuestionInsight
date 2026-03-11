from numpy import *
v=  array(eval(input()))
i = 0
cont = 0
while(i < size(n)):
		if(v[i]>80):
			print(i)
		cont += 1
		i += 1
print(cont)