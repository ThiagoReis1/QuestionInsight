n = input().upper()

i = 0
t = 0
a = 0
l = 0
p = 0
while i < len(n):
	if n[i] == "A":
		t = t + 19.90
		a += 1
	elif n[i] == "L":
		t = t + 3.50
		l += 1
	elif n[i] == "P":
		t = t + 4.25
		p += 1
	i += 1
print(round(t, 2), a, l, p)
		