from numpy import*

v = array(eval(input()))

s = 0
p = 0

for i in range(size(v)):
	if(v[i]< 5):
		s = s + 1
print(s)

r = zeros(s, dtype = int)

for k in range(size(v)):
	if (v[k] < 5):
		r[p]=k
		p = p + 1
print(r)