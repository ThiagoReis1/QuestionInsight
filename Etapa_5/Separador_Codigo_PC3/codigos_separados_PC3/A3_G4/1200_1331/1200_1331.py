from numpy import*
v = array(eval(input()))
v1 = size(v)
i = 0
cont = 0
while (i < size(v)):
	if (v[i] > 0):
		cont = cont + 1
	i = i + 1
print (cont)