from numpy import*
v = input("").upper()
a = 0
d = 0
c = 0
while a < len(v):
	if v[a] == "A" or v[a] == "E" or v[a] == "I" or v[a] == "I" or v[a] == "O" or v[a] == "U":
		c = c + 35.15
	else:
		d = d + 42.17
	a = a + 1
total = c + d
print(round(total , 2))