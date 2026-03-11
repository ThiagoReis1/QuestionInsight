from numpy import*
v = input("v: ").lower().split(',')
c = zeros(5,dtype=int)
for x in v:
	if(x == 'p'):
		c[0] = c[0] + 1
	elif(x == 'c'):
		c[1] = c[1] + 1
	elif(x == 'r'):
		c[2] = c[2] + 1
	elif(x == 'l'):
		c[3] = c[3] + 1
	else:
		c[4] = c[4] + 1
print(max(c))
print(c)