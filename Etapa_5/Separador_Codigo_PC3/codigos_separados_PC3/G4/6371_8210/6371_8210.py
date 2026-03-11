from numpy import*
c = array(eval(input("c: ")))

for i in range(size(c)):
	if c[i] !=0:
		c[i] = (c[i]-1)**2
	else:
		c[i] = 9**2
print(c)