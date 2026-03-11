from numpy import*

v= array(eval(input('tempo de chegada: ')))

i=0
while v[i]!=max(v):
	i=i+1
print(i)