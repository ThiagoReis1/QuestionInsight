from numpy import *
v = array(eval(input("")))
i = 0
t = 0
while v[i] != v[-1]:
	m = exp(float(v[i]))
	t = m + t
	i = i + 1
x = log(float(t) / exp(size(v)))
print(round(x, 2))