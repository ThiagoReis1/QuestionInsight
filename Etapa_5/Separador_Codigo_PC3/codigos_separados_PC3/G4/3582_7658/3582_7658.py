from numpy import *
s= array(eval(input(":")))
c= 0
i= 0
while i < size(s):
	if s[i]>160:
		c= c+s[i]-25
	else:
		c= c+s[i]
	i= i+1
print(round(c,2))