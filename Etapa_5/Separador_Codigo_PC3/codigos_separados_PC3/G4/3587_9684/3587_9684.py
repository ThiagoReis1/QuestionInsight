from numpy import *
v = array(eval(input("")))
t = size(v) -1
i = 0
s = 100
while i <= t:
	if v[i] == 1:
		s *= 5
	if v[i] == 2:
		s *= 3
	if v[i] == 3:
		s += 0
	if v[i] == 4:
		s /= 2
	i += 1
print(round(s, 2))