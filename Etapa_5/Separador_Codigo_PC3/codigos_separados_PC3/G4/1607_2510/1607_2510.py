from numpy import*
x = array(eval(input("ANDARES: ")))

i = 1
k = 0
from math import*
while i < size(x):
	k = k + (abs(x[i] - x[i-1])) * 3
	i+=1
print(k)