from numpy import*
v = array(eval(input()))
c = 0
b =0
i = 0
while (i < size(v)):
	if (v[i] >= 80):
		c += v[i] - (v[i]*0.15)
	if (v[i] < 80):
		b += v[i]
	i += 1
ab = c + b	
print (round(ab, 2))	