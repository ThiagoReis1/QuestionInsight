from numpy import *
v= array(eval(input("")))
soma=0
for i in v:
	soma=soma+i
	if soma>=55:
	   soma=0
print(soma)