from numpy import*
v = array(eval(input()))
p = 0
c = 0
while(c < size(v)):
	if(v[c] == 1):
		p = p + 80
	elif(v[c] == 2):
		p = p + 40
	elif(v[c] == 3):
		p = p + 20
	else:
		c = size(v)
	c = c + 1
print(p)