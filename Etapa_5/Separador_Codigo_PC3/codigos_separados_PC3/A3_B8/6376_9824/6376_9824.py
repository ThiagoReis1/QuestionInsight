from numpy import*

cestas = input(":").upper().split(",")
j = zeros(4, dtype = int)
jo = size(cestas)

for i in cestas:
	if i == "A":
		j[0] += 1 
	elif i == "B":
		j[1] += 1
	elif i == "C":
		j[2] += 1
	elif i == "D":
		j[3] += 1

print(j)
