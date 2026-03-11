from numpy import *
from math import *

v = array(eval(input()))
n = size(v)
m = sum(v) / size(v)
a = 0

for i in range(size(v)):
	a = a + (v[i] - m) ** 2

d = sqrt(a / (n - 1))
print(round(d, 3))
