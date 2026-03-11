x = float(input(': '))
k = int(input(': '))
n = 1
t = 0
while k >= n:
	c = x / (n*2-1)
	t += c
	n += 1
print(round(t,8))