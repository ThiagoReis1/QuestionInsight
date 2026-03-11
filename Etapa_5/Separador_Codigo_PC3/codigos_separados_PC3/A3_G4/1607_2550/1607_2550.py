from numpy import*
from math import*
v = array(eval(input(":")))
a=0
b=0
i=0
while(a<size(v)):
	b1= abs(v[i+1]-v[i])*3 + b
	i= i+1
	a=a+1
print(b)