from numpy import *
from numpy.linalg import *
a = array(eval(input()))
x = len(a)
i = 0
k = 0
j = 0
for i in range(x):
	if k < a[i]:
		k = a[i]
		j = i
print(j)