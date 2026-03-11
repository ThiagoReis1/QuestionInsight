from numpy import *
s = array(eval(input("digite: ")))
p = 0
for i in range(size(s)):
	if (s[i] <= 50):
		p = p + 1
print(p)

vs = zeros(p, dtype = int)
k = 0
for i in range(size(s)):
	
	if (s[i] <= 50):
		vs[k] = i
		k = k + 1
print(vs)
	
	
	
