from numpy import*
s = array(eval(input("")))


for i in range(size(s)):
	if s[i]== 9:
		s[i]= 0
	else:
		s[i] = s[i] + 1
		
print(s)