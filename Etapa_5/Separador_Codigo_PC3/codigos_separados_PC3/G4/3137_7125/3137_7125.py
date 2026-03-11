from numpy import *

num = array(eval(input(": ")))


m = 0
o = exp(size(num))

for x in range(size(num)):
	m = m + exp(num[x])
total = log(m/o)
print(round(total,2))