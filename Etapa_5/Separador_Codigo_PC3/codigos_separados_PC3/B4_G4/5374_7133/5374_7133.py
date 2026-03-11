from numpy import*
v = input("").upper()
i = 0
c = 0
while i< len(v):
	if v[i] == "A":
		c = c + 0.15
	elif v[i] == "E":
		c = c + 0.15
	elif v[i] == "I":
		c = c + 0.15
	elif v[i] == "O":
		c = c + 0.15
	elif v[i] == "U":
		c = c + 0.15
	else:
		c = c + 0.17
	i = i + 1
print(round(c, 2))
	
	