from numpy import *

v = input("produto: ")

i = 0
C = 0
E = 0
P = 0

while i<size(v) :
	if v[i] == "C":
		C = 10.50 + C
	C+=1

	if v[i] == "E":
		E = 8.74 + E
	E+=1

	if v[i] == "P":
		P = 17.90 + P
	P+=1
i+=1
print(round(i, 2))
print(c)
print(e)
print(p)