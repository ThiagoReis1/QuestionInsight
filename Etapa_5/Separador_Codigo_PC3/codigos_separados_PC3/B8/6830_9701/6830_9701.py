s = input("Digite H, L ou E: ").upper()
saldo = 0
for s in string:
	if s == "H":
		saldo += 3.85
		s = input().upper()
	elif s == "L":
		saldo += 2.95
		s = input().upper()
	elif s == "E":
		saldo += 7.90
		s = input().upper()
print(round(saldo, 2))