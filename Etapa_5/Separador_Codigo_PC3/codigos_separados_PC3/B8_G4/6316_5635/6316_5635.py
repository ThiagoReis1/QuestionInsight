from numpy import *
x = input().upper()
i = 0
c = 0
c1 = 0
c2 = 0
c3 = 0
while i <len(x):
	if x[i]=="D":
		c = c + 2.25
		c1 = c1 + 1
	elif x[i]=="S":
		c = c + 4.00
		c2 = c2 + 1
	elif x[i]=="I":
		c = c + 6.90
		c3 = c3 + 1
	i += 1
x = round(c, 2)
print(x,c1,c2,c3)
		