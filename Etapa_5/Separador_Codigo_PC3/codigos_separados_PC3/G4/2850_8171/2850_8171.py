from numpy import *
u=array(eval(input("")))
soma=0
for x in u:
	soma+=x
	if soma>55:
		soma=0
print(soma)