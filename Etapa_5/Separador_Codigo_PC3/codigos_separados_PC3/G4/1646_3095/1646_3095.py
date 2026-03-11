from numpy import*
v = array(eval(input()))
n = 0
for x in range(size(v)):
	if v[x] <= 50:
		n = n + 1
print(n)
s = zeros(n, dtype = int)
i = 0
for y in range(size(v)):
	if v[y] <= 50:
		s[i] = y
		i = i + 1
print(s)