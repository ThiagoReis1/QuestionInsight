from numpy import*
a = 200
v = array(eval(input()))
c = 0
while(c < size(v)):
	if(v.any() == 1):
		c = c + 1
		a = a*4
	elif(v.any() == 2):
		c = c + 1
		a = a*2
	elif(v.any() == 3):
	   c = c + 1
	elif(v.any() == 4):
		c = c + 1
		a = a/2
	print(round(a, 2))		