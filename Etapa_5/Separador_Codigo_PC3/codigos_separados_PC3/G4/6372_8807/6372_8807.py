from numpy import *

x = input("Digite: ").upper().split(',')

a = zeros(4, dtype=int)
for i in x:
	if i == "A":
		a[0] += 1
	elif i == "B":
		a[1] += 1
	elif i == "L":
		a[2] += 1
	else:
		a[3] += 1
print(a)