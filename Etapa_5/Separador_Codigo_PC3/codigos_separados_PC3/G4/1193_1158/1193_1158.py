from numpy import*
v = array(eval(input()))
c = 0
d = 0
e = 0
while(c<size(v)):
	if(v[c]>-100):
		d = d + 1
	c = c + 1
i = size(v)-d
v1 = array(zeros(i, dtype = float))
c = 0
while(c<size(v)):
	if(v[c]>-100):
		v1[e] = v[c]
	c = c + 1
print (v1)
	