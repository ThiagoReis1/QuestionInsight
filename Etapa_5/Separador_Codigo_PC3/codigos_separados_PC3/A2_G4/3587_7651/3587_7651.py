from numpy import*
v = array(eval(input()))
i = 0
c = 100

while (i < size(v)):
	if (v[i] == 1):
		c = c * 5
	if (v[i] == 2):
		c = c * 3
	if (v[i] == 3):
		c = c 
	if (v[i] == 4):
		c = c/2
	i += 1
print (round(c,2))	