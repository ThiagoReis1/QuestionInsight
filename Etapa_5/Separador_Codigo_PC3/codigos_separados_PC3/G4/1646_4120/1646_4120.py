from numpy import *
s = array(eval(input("valores de saque: ")))
c = 0
for i in range(size(s)):
	if(s[i] <= 50):
		c = c + 1
print(c)
j=-1
p = zeros(c, dtype = int)
for i in range(size(s)):
	if(s[i] <= 50):
		p[j] = i
print(p)

