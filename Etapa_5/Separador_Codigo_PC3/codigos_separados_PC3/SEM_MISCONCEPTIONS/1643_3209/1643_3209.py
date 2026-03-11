from numpy import *()
v = array(eval(input("")))
cont = 0
j = 0
for i in range(0, size(v)):
	if(v[i] >= 5):
		cont += 1
z = zeros(cont, dtype = int)
for i in range(0, size(v)):
	if(v[i] >= 5):
		z[j] = i
		j += 1
print(cont)
print(z)
		