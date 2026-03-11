from math import*
from numpy import*

b=input(":").split(',')

n=zeros(5, dtype=int)

for i in b:
	if ("AC"==i):
		n[0] = n[0]  + 1 
	elif ("AM"==i):
		n[1] = n[1]  + 1 
	elif ("PA"==i):
		n[2] = n[2]  + 1 
	elif ("RO"==i):
		n[3] = n[3]  + 1 
	elif ("RR"==i):
		n[4] = n[4]  + 1 

print(max(n))

print(n)

	
	