from numpy import*
n = array(eval(input()))
p = 0
c = 0
for i in range(size(n)):
	if (n[i]%2==0):
		p = p+1
z = zeros(p, dtype=int)
for j in range(size(n)):
	if(n[j]%2==0):
		z[c] = j
		c = c+1
print(p)
print(z)