from numpy import*

p = (input("Digite as letras: ")).upper()

c = 0
v = 0

while v < len(p):
	if p[v] == "A":
		c += 16.75
	elif p[v] == "L":
		c += 4.60
	elif p[v] == "P":
		c += 2.85
	v += 1
print(round(c, 2))
	