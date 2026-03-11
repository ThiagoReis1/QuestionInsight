produtos = input('Digite os produtos: ').upper()

b = 3.75
c = 7.90
e = 9.85
total = 0.0
b1 = 0
c1 = 0
e1 = 0

for i in produtos:
	if i == 'B':
		total = total + b
		b1 = b1 + 1
	elif i == 'C':
		total = total + c
		c1 = c1 + 1
	elif i == 'E':
		total = total + e
		e1 = e1 + 1

print(round(total, 2), b1, c1, e1)