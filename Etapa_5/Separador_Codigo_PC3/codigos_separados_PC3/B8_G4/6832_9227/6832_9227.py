v = input("")

i = 0
p = 0.0


while i < len(v):
	if v[i] == "H":
		p += 5.40
	elif v[i] == "C":
		p += 8.95
	elif v[i] == "L":
		p += 4.50
	i += 1
print(round(p, 2))