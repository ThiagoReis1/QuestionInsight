from numpy import*
com = array(eval(input()))
c = 0
s = sum(com)
d = 0
while(c < size(com)):
	if(com[c] > 80):
		d = d + 5
	c = c + 1
s = s - d
print(round(s, 2))