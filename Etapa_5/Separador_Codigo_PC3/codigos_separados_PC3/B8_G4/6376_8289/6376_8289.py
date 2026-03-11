from numpy import * 

pont = input(":").upper().split(",")
j = zeros(4, dtype=int)

for i in range(size(pont)):
	if pont[i]  == "A":
		j[0] += 1 
	elif pont[i] == "B":
		j[1] += 1 
	elif pont[i] == "C":
		j[2] += 1 
	elif pont[i] == "D":
		j[3] += 1

print(j)