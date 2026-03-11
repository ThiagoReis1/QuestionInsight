from numpy import*
s = array(eval(input()))
s1 = zeros(size(s), dtype=int)

for i in range(size(s)):
	if s[i] == 0:
		s1[i] = (9)**2
		
	else:
		s1 [i] =	(s[i] - 1)**2
	
print(s1)
