from numpy import*
v = array(eval(input()))
kg=217
i = 0
cont = 0
while (i < size(v)):
	if (v[i] <kg):
		cont = cont + 1
	i +=1
print (kg)
	
print (cont)