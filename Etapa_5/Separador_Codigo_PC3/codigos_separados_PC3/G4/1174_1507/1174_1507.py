n = int(input("digite um numero:"))
p = 3
s = 0
r = 1
while r <= n:
	if r%2 == 0:
		s = s + ((r**3)/ (9 + p))
	else:
		s = s - ((r**3)/(9 + p))
	r = r + 1
	p = p + 2
print(round(s, 8))