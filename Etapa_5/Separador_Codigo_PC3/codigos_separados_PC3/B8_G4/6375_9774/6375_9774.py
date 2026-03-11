from numpy import *

vt = input("Voto: ").upper().split(",")
a = zeros(4, dtype=int)

for v in vt:
	if v == "A":
		a[0] += 1
	elif v == "B":
		a[1] += 1
	elif v == "C":
		a[2] += 1
	elif v == "D":
		a[3] += 1

print(a)