from numpy import*

v = array(eval(input()))
i = 0
c = 0

while i < size(v):
	if v[i] > 80:
		v[i] = v[i]*0.15
	i = i + 1
c = sum(v)
print(round(c,2))

	