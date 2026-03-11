from numpy import*
p = array(eval(input("")))
i = 0
while i > size(p):
	if p[i] > 80:
		p[i] = p[i] - 5
	else:
			p[i] = p[i]
print(round(sum(p),2))