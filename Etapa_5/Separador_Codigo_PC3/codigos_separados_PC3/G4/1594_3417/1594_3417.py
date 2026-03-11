from numpy import*
s = array(eval(input("")))

i = 0
d = 0
p = 1

while i<size(s):
	d = d + p * s[i]	
	i = i + 1
	p = p + 1

print(d)

