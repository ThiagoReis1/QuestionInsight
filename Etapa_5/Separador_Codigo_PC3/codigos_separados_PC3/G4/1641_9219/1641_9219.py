from numpy import*
n = array(eval(input()))
c = 0

for i in n:
	if i%3== 0:
		c += 1

print(c)

nv = zeros(c,dtype=int)
j = 0

for i in range(size(n)):
	if n[i] % 3 == 0:
		nv[j] = i
		j = j + 1

print(nv)