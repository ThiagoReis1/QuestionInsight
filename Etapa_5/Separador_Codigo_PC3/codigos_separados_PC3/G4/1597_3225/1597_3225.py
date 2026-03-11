from numpy import*

c = array(eval(input()))
i = 0
while(i < size(c)):
	if (c[i] > 80):
		c[i] = c[i] - 5
	i = i + 1
vt = sum(c)
print(round(vt, 2))
