from numpy import *
x = array(eval(input()))
cont=0
for i in x:
	if i == 0:
		cont = 0
	else:
		cont = cont + i

print(cont)