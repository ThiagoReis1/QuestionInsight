from numpy import *

v = input("").upper()

i = 0
c = 0
while i < len(v):
	if v[i] == "A":
		c = c + 1.12
	elif v[i] == "E":
		c = c + 1.12
	elif v[i] == "I":
		c = c + 1.12
	elif v[i] == "O":
		c = c + 1.12
	elif v[i] == "U":
		c = c + 1.12
	else:
		c = c + 1.18
	i = i + 1
print(round(c, 2))