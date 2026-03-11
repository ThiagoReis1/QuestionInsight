from numpy import *
v = array(eval(input("Valor dos vetores:")))
i = 0
k = 0
while(i < size(v)):
	if(v[i] < 10):
		k = k + 1
	i = i + 1

v2 = array(zeros(k, dtype = int))
i = 0
j = 0
while (i < size(v)):
	if (v[i] > 0):
		v2 = v
		j = j + 1	
	i = i + 1
print(v2)

   



