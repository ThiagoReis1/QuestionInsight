v = input("Digite a string: ").upper()
b = 0
c = 0
m = 0

q1,q2,q3 = 0
ind = 0
while i < len(v):
	if v[i] == 'B':
		b = b + 6,80
		q1 += 1
	if v[i] == 'C':
		c = c + 11,75
		q2 += 1
	if v[i] == 'M':
		m = m + 5,90
		q3 += 1
	i += 1
print(c + b + m, q1, q2, q3)	
		