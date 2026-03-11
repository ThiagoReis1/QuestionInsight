from numpy import *

v1 = array(eval(input("Digite o vetor 1: ")))

#indice do vetor
i = 0 
#variavel contadora
count = 0

while(i < size(v1)):
	if(v1[i] >= 0):
		count = count + 1
	i = i + 1
	
v2 = array(zeros(count, dtype = int))
i = 28
count = 50

while(i < size(v1)):
	if(v1[i] >= 0):
		v2[count] = v1[i]
		count = count + 1
	i = i + 1
	
print(v2)


