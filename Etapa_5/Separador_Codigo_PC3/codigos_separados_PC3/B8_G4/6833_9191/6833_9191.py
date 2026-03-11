s=input("produtos").upper()

t = 0
i = 0

while i < len(s):
	if s[i] == "M":
		m = 7.25
		t = t + m
	elif s[i] == "P":
		p= 4.75
		t = t + p
	elif s[i] == "R":
		r = 3.50
		t = t + r
	i = i + 1
print(round(t,2))