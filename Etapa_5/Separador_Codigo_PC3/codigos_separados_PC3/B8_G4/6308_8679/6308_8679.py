v = str(input())
i = 0
a = 0
a2 = 0
l = 0
l2 = 0
p = 0
p2 = 0

while i < len(v):
	if v[i] == "A":
		a = a + 16.75
		a2 = a2 + 1
	elif v[i] == "L":
		l = l + 4.6
		l2 = l2 + 1
	elif v[i] == "P":
		p = p + 2.85
		p2 = p2 + 1
	i = i + 1
s = (a + l + p)
print(round(s, 2), a2, l2, p2)