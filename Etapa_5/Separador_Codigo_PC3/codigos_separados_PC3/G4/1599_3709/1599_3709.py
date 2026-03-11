from numpy import*
v = array(eval(input()))
p = zeros(len(v), dtype=float)
j = zeros(len(v), dtype=float)
k = 0
l = 0
for i in v:
	if i > 80:
		p[k] = i - (i * 15/100)
		k += 1
	else:
		j[l] = i
		l += 1
print(round((sum(p) + sum(j)), 2))