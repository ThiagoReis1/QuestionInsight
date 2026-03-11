from numpy import *

v = input().upper().split(",")

z = zeros(4, dtype=int)

for i in v:
	if i == "A":
		z[0] += 1
	if i == "B":
		z[1] += 1
	if i == "L":
		z[2] += 1
	if i == "H":
		z[3] += 1
print(z)
	