from numpy import *

s = array(eval(input('vetor:   ')))

for i in range(size(s)):
	if s[i]==s[i]:
		s[i] = s[i] * 2
print(s)
	