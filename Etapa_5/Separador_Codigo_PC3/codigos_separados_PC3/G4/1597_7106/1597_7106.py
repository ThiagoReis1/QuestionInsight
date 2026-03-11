from numpy import *

v = eval(input())
i = 0
desc = 0

while (i < size(v)):
	if (v[i] > 80):
		desc = desc +5


	i = i + 1
v = sum(v)-desc
print(round(v, 2))