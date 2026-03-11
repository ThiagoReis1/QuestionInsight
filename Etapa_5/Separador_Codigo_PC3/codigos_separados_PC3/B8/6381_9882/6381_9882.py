from numpy import*

cartas = input("insira: ").upper().split(",")
v = zeros(4, dtype=int)

for i in cartas:
	if i == "C":
	   v[0] += 1
	elif i == "O":
		v[1] += 1
	elif i == "P":
		v[2] += 1
	elif i == "E":
		v[3] += 1
print(v)