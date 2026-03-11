from numpy import *

x = input("").upper()
x = x.split(',')


vt = zeros(5, dtype=int)

for i in range(size(x)):
	if x[i] == "P":
		vt[0] += 1
	elif x[i] == "C":
		vt[1] += 1
	elif x[i] == "M":
		vt[2] += 1
	elif x[i] == "V":
		vt[3] += 1
	elif x[i] == "A":
		vt[4] += 1
print(max(vt))
print(vt)