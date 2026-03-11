from numpy import*
c= array(eval(input("digite o codigo: ")))
			
for i in range(size(c)):
	if (c[i] == 0):
		c[i] = 0
	else:
		c[i]*= 2
print(c)

