from numpy import *
v = array(eval(input()))

i = 0
m = 0
while i < size(v):
	m = m + (v[i]) ** 2
	i = i + 1
print(round((m / size(v)) ** 0.5, 2))