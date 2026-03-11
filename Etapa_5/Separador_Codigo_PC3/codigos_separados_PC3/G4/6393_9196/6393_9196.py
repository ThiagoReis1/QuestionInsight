from numpy import*
c= array(eval(input("codigo:")))

for i in range(size(c)):
	if c[i]== 9:
		c[i]= 0
	else:
		c[i]= (c[i]+1)** 3
print(c)