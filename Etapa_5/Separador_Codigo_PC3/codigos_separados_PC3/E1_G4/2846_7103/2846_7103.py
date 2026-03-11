from numpy import*
c = array(eval(input()))

for i in range(size(c)):
	if c[i]==0 or c[i]==1 or c[i]==2 or c[i]==3 or c[i]==4 or c[i]==5 or c[i]==6 or c[i]==7 or c[i]==8 or c[i]==9:
		c[i] = c[i] * 2
print(c)