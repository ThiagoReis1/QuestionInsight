from numpy import*

n = array(eval(input()))

h = 0
s = 0

for i in range(size(n)):
	if(n[i] < 5):
		h = h + 1
print(h)

nv = zeros(h, dtype = int)

for j in range(size(n)):
	if(n[j] < 5):
		nv[s] = j
		s = s + 1
print(nv)
	
		