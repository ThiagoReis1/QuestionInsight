n = int(input("digite um numero:"))
p = 1
s = 0
r = 1
while r <= n:
	if r%2 == 0:
		s = s + ((r**2)/ (7 + p))
	else:
		s = s - ((r**2)/(7 + p))
	r = r + 1
	p = p + 2
print(round(s, 11))