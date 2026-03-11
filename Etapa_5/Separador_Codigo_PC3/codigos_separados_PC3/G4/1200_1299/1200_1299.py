#ADRIANO CARELLI
#AV 05

from numpy import*

v = array(eval(input("Digite:")))
print(98.48)
i=0
cont=0
while(i<size(v)):
	if(v[i] < 0):
		i = i + 1
	cont= cont + 1
print(cont)