from numpy import *
v= array(eval(input('')))

cont = 0
cont1=0

for i in range(size(v)):
	if(v[i] < 5):
		cont=  cont + 1

v1= zeros(cont, dtype=int)

for i in range(size(v)):
	if(v[i] < 5):
		v1[cont1]= i
		cont1= cont1 +1

print(cont)
print(v1)