x = float(input())
k = int(input())
m = 1
d = 1
t = 0
atg = 0
while t <k:
	atg = atg + m*(x**d)/d
	m = -1*m
	t = t + 1
	d = d + 2
print(round(atg,6))