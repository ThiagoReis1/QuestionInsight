x = input("SECAO?: ")

i = 0
H = 0
L = 0
E = 0
q = 0
c = 0
F = 0

while i < len(x):
	if x[i] == "H":
		H = H + 3.85
		q = q + 1
	elif x[i] == "L":
		L = L + 2.95
		c = c + 1
	elif x[i] == "E":
		E = E + 7.90
		F = F + 1
	i = i + 1
	

s = H + L + E
print(round(s, 2 ),q,c,F)
	