from numpy import *
s = array(eval(input("")))
for x in range(size(s)):
	if s[x] == 0:
		predecessor = 9	
	else:
		predecessor = s[x] -1
	s[x] = predecessor**3
print(s)