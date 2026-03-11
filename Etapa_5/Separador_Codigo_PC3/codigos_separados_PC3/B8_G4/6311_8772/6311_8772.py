s = input().upper()
v = 0
i = 0
p = 0
c = 0
e = 0

while i < len(s):
	if s[i] == "C":
		v = v + 10.5
		c += 1
	elif s[i] == "E":
		v = v + 8.75
		e += 1
	elif s[i] == "P":
		v = v + 17.9
		p += 1
	i += 1
print(round(v,2), c, e, p)
