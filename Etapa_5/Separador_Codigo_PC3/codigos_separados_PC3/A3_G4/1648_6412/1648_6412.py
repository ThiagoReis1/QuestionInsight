from numpy import *
p = array(eval(input('Frequencia: ')))
r = 0
n = 0
m = 0
k = 0
for i in range(size(p)):
	if p[i] < 70:
		r = r + 1
		n = n + 1
s = zeros(n , dtype=int)
for j in range(size(p)):
	if p[j] < 70:
		m = m + 1
		s[m - 1] = j
print(r)
print(s)