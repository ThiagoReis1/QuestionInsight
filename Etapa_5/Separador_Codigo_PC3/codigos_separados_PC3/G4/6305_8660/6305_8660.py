from numpy import *
x = input()
i = 0
c = 0
c1 = 0
c2 = 0
c3 = 0
while i <len(x):
	if x[i] == "H":
		c = c + 3.85
		c1 = c1+1
	if x[i] == "L":
		c = c + 2.95
		c2 = c2 +1
	if x[i] == "E":
		c = c + 7.90
		c3 = c3 + 1
	i = i+1
x = round(c,2)
print(x,c1, c2,c3)