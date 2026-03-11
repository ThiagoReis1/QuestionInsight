a = int(input("em gramas: "))
b = int(input("em anos: "))

q = a
m = 0
n = 0

while(n<b):
	m = q * 0.05
	q = q - m
	n = n + 1
	print(round(q, 2))