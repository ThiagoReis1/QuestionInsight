from numpy import *

food = input(":").upper().split(",")
sup = zeros(4, dtype=int)

for i in food:
	if i == "A":
		sup[0] += 1
	elif i == "B":
		sup[1] += 1
	elif i == "L":
		sup[2] += 1
	elif i == "H":
		sup[3] += 1
print(sup)