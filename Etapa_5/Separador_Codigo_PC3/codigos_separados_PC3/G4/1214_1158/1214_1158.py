from numpy import*
v = array(eval(input()))
c = 0
m = 0
r = 217
while(c < size(v)):
	if(v[c] < r):
		m = m + 1;
	c = c +1
print(r)
print(m)
	