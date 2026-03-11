s = input("Digite os produtos: ").upper()
i = 0
a = 0
l = 0
p = 0
sm = 0

while i < len(s):
	if s[i] == "A":
		sm = sm + 16.75
		a += 1
	elif s[i] == "L":
		sm = sm + 4.60
		l += 1
	elif s[i] == "P":
		sm = sm + 2.85
		p += 1
	i += 1

print(round(sm, 2), a, l, p)