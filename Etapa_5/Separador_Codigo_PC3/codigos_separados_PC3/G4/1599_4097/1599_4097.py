from numpy import*
v = array(eval(input("V: ")))
d = 15/100
i = 0
while (size(v) > i):
	if(v[i] > 80):
		v[i] = v[i] - v[i] * d
	else:
		v[i] = v[i]
	i = i + 1
vt = sum(v)
print(round(vt, 2))