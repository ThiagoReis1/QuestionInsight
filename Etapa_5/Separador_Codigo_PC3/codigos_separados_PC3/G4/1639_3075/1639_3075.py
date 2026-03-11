from numpy import *
t = array(eval(input()))

p = 0 
for num in t:
	if (num %2 == 0):
		p = p + 1
ind = zeros(p, dtype=int)
i = 0
w = 0
for n in t:
	if(n%2 == 0):
		ind[w] = i
		w = w + 1
	i = i + 1
print(p)
print(ind)