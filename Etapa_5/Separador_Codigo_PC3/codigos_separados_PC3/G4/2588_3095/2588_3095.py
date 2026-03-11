from numpy import*
v = array(eval(input()))
lim = v[0]
n = 0
for x in range(size(v)):
	if x != 0:
		if lim * 0.2 < v[x] - lim < lim * 0.5:
			print(x)
			n = n + 1
print(n)