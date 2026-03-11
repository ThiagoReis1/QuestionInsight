from numpy import*

v = array(eval(input("")))
c = 0
d = 0
for i in range(size(v)):
	if v[i]%3 == 0:
		c += 1
v1 = zeros(c,dtype = int)
for x in range(size(v)):
	if v[x]%3 == 0:
		v1[d] = x
		d += 1
	
print(c)
print(v1)