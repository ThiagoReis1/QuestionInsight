from numpy import *
st = input("Codigos: ").upper()
i = 0
c = 0
d = 0
j = 0
t = len(st)-1
while i <= t:
	if st[i] == "C":
		c += 1
	elif st[i] == "E":
		d += 1
	elif st[i] == "P":
		j += 1
	i += 1
m = c*10.50 + d*8.75 + j*17.90

print(round(m,2))