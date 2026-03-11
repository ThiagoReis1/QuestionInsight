from numpy import*

s = input("pacientes: ").upper().split(",")

ab = array([0,0,0,0])

for i in s:
	if i == "O":
		ab[0] = ab[0] + 1
	elif i == "D":
		ab[1] = ab[1] + 1
	elif i == "N":
		ab[2] = ab[2] + 1
	elif i == "C":
		ab[3] = ab[3] + 1
print(ab)