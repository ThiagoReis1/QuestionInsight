from numpy import*
c = input("Digite as compras: ").upper()
i = 0
t = 0
m = 0
p = 0
r = 0
while i < len(c):
	if c[i] == "M":
		m = m + 1
		t = t + 7.25
	elif c[i] == "P":
		p = p + 1
		t = t + 4.75
	elif c[i] == "R":
		r = r + 1
		t = t + 3.50
	i = i + 1
print(round(t,2),m,p,r)
	