from numpy import*

v = array(eval(input()))
s = 0

for i in range(size(v)):
	if(v < 9):
		s = s - 1
print(s)