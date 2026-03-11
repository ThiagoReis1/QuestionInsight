from numpy import *
v = array(eval(input(':')))
i = 0
t = 100
while i < size(v):
	if v[i] == 1:
		t = t
	elif v[i] == 2:
		t = t * 2
	elif v[i] == 3:
		t = t / 3
	elif v[i] == 4:
		t = t * 4
	elif v[i] == 5:
		t = t / 5
	elif v[i] == 6:
		t = t * 6
	i = i + 1
print(round(t,2))