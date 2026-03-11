from numpy import *
from math import *

v = array(eval(input("digite o vetor: ")))
total2 = 0
total = 0
i = 0
while(i < size(v)):
	if(v[i]>80):
		total = total + (v[i] - 5)
		i = i + 1
	elif(v[i]<=80):
		total2 = total2 + v[i]
		i = i + 1
total3 = total + total2
print(round(total3, 2))