from numpy import *
a = input("").upper().split(",")
t = size(a)
x = zeros(4, dtype= int)
for i in range(size(a)):
	if a[i] == "E":
		x[0] += 1
	elif a[i] == "V":
		x[1] += 1
	elif a[i] == "A":
		x[2] += 1
	elif a[i] == "D":
		x[3] += 1
print(x)