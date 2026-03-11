from numpy import *
from math import *

v = array(eval(input()))
i = 0 
j = 0 

while i<size(v):
	if v[i] < -50 or v[i] > 20:
		j = j + 1 
	i = i + 1 

v1 = array(zeros(size(v)-j), dtype=float)
#print(v1)


i = 0 
j = 0 
while i < size(v):
	if v[i] < 20 and v[i] > -50:
		v1[j] = v[i]
		j = j + 1 
	i = i + 1 
print(v1)