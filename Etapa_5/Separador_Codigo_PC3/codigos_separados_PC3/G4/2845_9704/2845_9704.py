from numpy import *

s = array(eval(input()))
for i in range(0,size(s)):
	if s[i] == 9:
			s[i] = 0
	elif s[i] == 7:
			s[i] = 8
	else:
		s[i] += 1 
print(s)