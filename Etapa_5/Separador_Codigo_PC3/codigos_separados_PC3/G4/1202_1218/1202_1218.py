from numpy import *
v1 = array(eval(input("Informe as temperaturas:")))
n = size(v1)
v2 = array(zeros(n,dtype=float))
i = 0
j = 0
while(i < size(v1)):
	i = i + 1
	while(v1[i] > 22):
		v2[j] = v1[i]
		while(j < i):
			j= j + 1
		print(v2)