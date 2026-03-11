from numpy import *
v = array(eval(input("tempos de chegada: ")))
i = 0
while v[i] != min(v):
	i = i + 1
print(i)