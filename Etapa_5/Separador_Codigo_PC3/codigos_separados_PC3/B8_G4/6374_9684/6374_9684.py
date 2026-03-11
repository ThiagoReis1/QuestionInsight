from numpy import *
s = input("").upper().split(",")
x = zeros(4, dtype = int)
for a in s:
	if a == "O":
		x[0] += 1
	elif a == "D":
		x[1] += 1
	elif a == "N":
		x[2] += 1
	elif a == "C":
		x[3] += 1
print(x)