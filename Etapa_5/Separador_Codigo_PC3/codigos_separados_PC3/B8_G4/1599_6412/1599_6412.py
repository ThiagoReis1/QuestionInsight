from numpy import *
v = array(eval(input(':')))
i = 0
t = 0
while i < size(v):
	if v[i] > 80:
		t = t + v[i] * (85/100)
	elif v[i] <= 80:
		t = t + v[i]
	i = i + 1
print(round(t,2))