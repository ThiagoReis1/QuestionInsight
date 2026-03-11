from numpy import *
a = input("").upper()
s = 0
for i in range(len(a)):
	if a[i] == "E":
		s += 1
print(s)