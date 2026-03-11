v = input("String: ").upper()
i = 0
p = 0
while (i < len(v)):
	if (v[i] == "A") or (v[i] == "E") or (v[i] == "I") or (v[i] == "O") or (v[i] == "U"):
		p = p + 0.15
	else:
		p = p + 0.17
	i = i + 1
print(round(p, 2))