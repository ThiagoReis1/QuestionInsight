# Talita Passos
# 11 de Agosto de 2016
# Avaliacao 5 - Ex 02

from numpy import *

v1 = array(eval(input("Digite as temperaturas: ")))

k = 50
i = 0
count = 0 

while(i < size(v1)):
	if(v1[i] > k):
		count = count + 1
	i = i + 1 
	
v2 = array(zeros(size(v1) - count, dtype = float))

i = 0 
count = 0

while(i < size(v1)):
	if(v1[i] < k):
		v2[count] = v1[i]
		count = count + 1
	i = i + 1

print(v2)