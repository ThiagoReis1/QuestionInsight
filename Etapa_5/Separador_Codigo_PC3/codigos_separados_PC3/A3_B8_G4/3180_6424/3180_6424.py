from numpy import *
s = array(eval(input()))
f = zeros(4,dtype=int)
c2 = 0
c4 = 0
c3 = 0
c1 = 0
for i in range(size(s)):
	if s[i] == 2:
		c2 += 1
	elif s[i] == 4:
		c4 += 1
	elif s[i] == 3:
		c3 += 1
	elif s[i] == 1:
		c1 += 1
f = array([c1,c2,c3,c4])
print(f)