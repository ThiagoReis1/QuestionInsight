from numpy import * 
c = array(eval(input('custos: ')))
i = 0
b = 0
while i < size(c):
	if c[i] >= 80:
		b = b + 1
		i = i + 1
	else:
		b = b + 0
		i = i + 1
print(round((sum(c) - b * 5),2))