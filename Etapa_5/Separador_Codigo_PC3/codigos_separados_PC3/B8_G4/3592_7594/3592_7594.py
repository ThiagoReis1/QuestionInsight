from numpy import*
d = array(eval(input()))
p = 100
i = 0

while i < size(d):
	if d[i]%2 == 0:
		p = p*d[i]
	elif d[i]%2 != 0:
		p = p/d[i]
	i += 1

print(round(p,2))