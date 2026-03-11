p = input(" ").upper()
i = 0
total = 0

while i<len(p):
	if p[i]=="H":
		total = total + 3.85
	if p[i]=="L":
		total = total + 2.95
	if p[i]=="E":
		total = total + 7.90
	i += 1
print(round(total, 2))