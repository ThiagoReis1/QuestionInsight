from numpy import *
v = array(eval(input("Digite o vetor: ")))
i = 0
l = size(v)
n = 0
while(i < size(v)):
	if(v[i] < -100):
		n = n + 1
	i = i + 1
l = size(v) - n
i = 0
k = 0
v2 = array(zeros(l, dtype = float))
while(i < size(v)):
	if(v[i] > -100):
		v2[k] = v[i]
		k = k + 1
	i = i + 1
print(v2)