from numpy import *
v = array(eval(input("vetor de notas: ")))
p = [3, 2, 4, 1, 3]
i = 0
s = 0
d = 0
while i < size(v):
	s = s + (v[i] * p[i])
	d = d + (p[i])
	i = i + 1
print(round(s / d, 2))

	