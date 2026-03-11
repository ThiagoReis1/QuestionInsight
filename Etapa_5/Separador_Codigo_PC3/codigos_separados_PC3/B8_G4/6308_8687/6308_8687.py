compra = input("A, L ou P: ").upper()

i = 0
j = 0
a = 0
l = 0
p = 0

while i < len(compra):
	if compra[i] == "A":
		a += 1
		j = j + 16.75
	elif compra[i] == "L":
		l += 1
		j = j + 4.6
	elif compra[i] == "P":
		p += 1
		j = j + 2.85
	i += 1
print(round(j,2), a, l, p)