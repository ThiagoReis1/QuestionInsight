from numpy import *
x = input().upper()
i = 0
c = 0
c1 = 0
c2 = 0
c3 = 0
while i < len(x):
	if x[i] == "A":
		c = c + 19.90
		c1 = c1 + 1
	elif x[i] == "L":
		c = c + 3.50
		c2 = c2 + 1
	elif x[i] == "P":
		c = c + 4.25
		c3 = c3 + 1
	i = i+1
x = round(c, 2)
print(x,c1,c2,c3)