from numpy import *
from math import *

v = array(eval(input()))
s = 0
n = size(v)

for i in range(size(v)):
	
	s = s + v[i]

m = s / n

s1 = 0

for i in range(size(v)):
	
	s1 = s1 + ((v[i] - m) ** 2)

d = sqrt(s1 / (n - 1) )

print(round(d,3))