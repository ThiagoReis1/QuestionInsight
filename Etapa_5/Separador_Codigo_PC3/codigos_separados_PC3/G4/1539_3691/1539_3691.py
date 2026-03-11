x = float(input())
k = int(input())
i = m = 1
p = r = 0
while i <= k:
	r = r + m*(x**p)
	m = m*(-1)
	p = p + 1
	i = i + 1
print(round(r,7))