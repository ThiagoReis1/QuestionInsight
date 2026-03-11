from numpy import*
b1 = array(['A','E','I','O','U'])
x = input(': ').upper()
i = c = p1 = p = 0
while i < len(x):
	while c < size(b1):
		if x[i] == b1[c]:
			p1 = 1
		c += 1
	if p1 == 1:
		p += 0.15
	else:
		p += 0.17
	i += 1
	c =0
	p1 = 0
print(round(p,2))