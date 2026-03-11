from numpy import*

v = array(eval(input("vetor")))
c = 0

for i in range(0, size(v)):
	if v[i] >= 2000:
		c += 1

print(c)

j = 0
m = zeros(c, dtype=int)
for i in range(0,size(v)):
	if v[i] >= 2000:
		m[j] = i
		j += 1
print(m)