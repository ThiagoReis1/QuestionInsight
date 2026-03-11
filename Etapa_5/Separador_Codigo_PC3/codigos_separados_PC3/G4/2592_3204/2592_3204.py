from numpy import*
v = array(eval(input()))
b = 0
c = 0

h = v[0]+(v[0]*0.6)


for i in v:
	if(i>=h):
		print(b)
		b = b+1
		c = c+1
	elif(i>=h):
		c = c+1
	else:
		b = b+1
print(c)	


