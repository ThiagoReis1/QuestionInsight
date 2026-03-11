V = input("digite a sequencia dos produtos: ").upper()
i = 0
m = 0
s = 0
q1,q2,q3 = 0,0,0
ind = 0

while s < len(v):
	if v[ind] == "I":
		i = i + 3.75
		q1 += 1
	elif v[ind] == "M":
		m += 4.50
		q2 += 1
	elif v[ind] == "S":
		s += 2.90
		q3 += 1
print(m + i + ind, q1, q2, q3)
