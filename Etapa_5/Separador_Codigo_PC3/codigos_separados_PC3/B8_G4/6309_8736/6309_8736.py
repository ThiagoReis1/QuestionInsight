from numpy import *

v = input("PAYSANDUU U U U U U U : ")
i = 0
h = 0
c = 0
l = 0
acm = 0

while len(v) > i :
	if (v[i] == "H"):
		h = h + 1
		acm = acm + 5.40
	elif (v[i] == "C"):
		c = c + 1
		acm = acm + 8.95
	elif (v[i] == "L"):
		l = l + 1
		acm = acm + 4.50
	i = i + 1
print(round(acm,2), h , c , l)
