from numpy import*
c = array(eval(input()))
i = 0
p = 0
while i < size(c):
	if c[i]>=80:
		p += c[i]-c[i]*15/100
	else:
		p += c[i]
	i += 1
print(round(p,2))