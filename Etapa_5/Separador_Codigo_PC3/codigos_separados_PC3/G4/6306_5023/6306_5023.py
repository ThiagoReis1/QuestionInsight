b = input("alimentos: ").upper()
i = 0
t = 0
a = 0
l = 0
p = 0
while i < len(b):
	if (b[i] == "A"):
		t = t + 19.90
		a = a + 1
	if (b[i] == "L"):
		t = t + 3.50
		l = l + 1
	if (b[i] == "P"):
		t = t + 4.25
		p = p + 1
	i = i + 1
print(round(t,2),a,l,p)