from numpy import *

s = array(eval(input()))
s1 = zeros(size(s), dtype = int)

for i in range (size(s)):
	if s[i] == 9:
		s1[i] = 0
	else: 
		s1 [i] = s[i] +1
print(s1)
