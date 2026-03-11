p = input(" ")

c = 0 
v = 0

while c < len(p):
	if p[c] == "H":
		v += 5.40
	elif p[c] == "C":
		v += 8.95
	elif p[c] == "L":
		v += 4.50
	c += 1
print(round(v, 2))