pr= input("p: ").upper()
B = 0
C = 0
E = 0
i = 0
while i < len(pr):
	if pr[i] == "B":
		B += 1
	elif pr[i] == "C":
		C += 1
	elif pr[i] == "E":
		E += 1
	i += 1
pb = B *3.75
pc = C * 7.9
pe = E * 9.85

print(round(pb+pc+pe, 2),B,C,E)