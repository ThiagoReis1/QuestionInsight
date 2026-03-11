from numpy import *
n=  array(eval(input()))
i = 0
cont = 0
while(i < size(n)):
		if(cont >75):
			n[i] = cont - 80 
		cont = cont + n[i]
		i = i + 1
print(cont)