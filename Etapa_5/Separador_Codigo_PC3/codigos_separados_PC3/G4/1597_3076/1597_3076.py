from numpy import*

p = array(eval(input()))

i = 0
a = 0

while(i < size(p)):
	if(float(p[i]) > 80.0):
		p[i] = p[i] - 5
	else:
		p[i] = p[i]
	a = a + p[i]
	i = i + 1

print(round(a, 2))



