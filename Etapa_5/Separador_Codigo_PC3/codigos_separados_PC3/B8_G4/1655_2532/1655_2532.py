from numpy import *
x = input("estados:").split(',')
c = zeros(5,dtype=int)
for i in range(size(x)):
	if(x[i] == "AC"):
		c[0] =  c[0] + 1
	elif(x[i] == "AM"):
		c[1] = c[1] + 1
	elif(x[i] == "PA"):
		c[2] = c[2] + 1
	elif(x[i] == "RO"):
		c[3] = c[3] + 1
	elif(x[i] == "RR"):
		c[4] = c[4] + 1
print(max(c))
print(c)

