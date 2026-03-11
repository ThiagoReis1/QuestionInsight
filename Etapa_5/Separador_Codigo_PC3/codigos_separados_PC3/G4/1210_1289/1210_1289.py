from numpy import *
v=array(eval(input("insira o v: ")))
print(74.08)
i=0
j=0
while i<size(v):
	if v[i]<74.08:
		j=j+1
	i=i+1
print(j)