from numpy import *
saque = array(eval(input("")))
cont = 0
j = 0
for i in range(0, size(saque)):
	if(saque[i] >= 2000):
		cont += 1
z = zeros(cont, dtype = int)
for i in range(0, size(saque)):
	if(saque[i] >= 2000):
		z[j] = i
		j += 1
print(cont)
print(z)