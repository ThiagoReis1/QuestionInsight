from numpy import*

v = array(eval(input()))
s = 0
ind = []

for i in range(size(v)):
	if(v[i] >= 2000):
		s = s + 1
		ind.append(i)
a = zeros(size(ind), dtype=int)
a = a + ind
print(s)
print(a)