from numpy import * 

v = array(eval(input("MDS TOMEI")))

i = 0 
c = 0
for i in range(size(v)):
	if v[i] >= 70:
		c += 1
print(c)
d = zeros(c, dtype = int)
s = 0 
for z in range(size(v)):
	if v[i] >= 70:
		c += 1
		d[i] = s 
		i += 1
print(d)