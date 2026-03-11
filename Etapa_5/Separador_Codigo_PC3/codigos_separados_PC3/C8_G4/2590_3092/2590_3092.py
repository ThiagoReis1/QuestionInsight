from math import*
from numpy import*

v= array(eval(input("v:")))
i=1
n=0

for i in range(size(v)):
	if v[i]<v[0]:
		print(i)
		n=n+1
	i=i+1
print(n)