from numpy import *
s = array(eval(input("")))
i = 0 
c = 0 
for v in range(size(s)):
	if v <= 20:
		c += 1
print(c)
d = zeros(c, dtype = int)
c = 0
for v in range(size(s)):
	if v >= 20:
		d[i] = s
		i += 1
	c += 1
print(d)